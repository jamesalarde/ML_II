# import requirements
import pandas as pd
import google.generativeai as genai
import os
from langchain import PromptTemplate
from langchain.chains import SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain

# setup API
os.environ['GOOGLE_API_KEY'] = 'AIzaSyA5I9zdE44pHsp33RlkiKbrKQJapqosmX0'

# create prompt template 1
product_description = PromptTemplate(
    input_variables=['product_name', 'product_information'],
    template='Generate a three-sentence product description for the product called {product_name}. Here is the information regarding this product: {product_information}.'
)

description_llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', temperature=0)
description_chain = LLMChain(llm=description_llm, prompt=product_description, output_key='description_text')

# create prompt template 2
tone = PromptTemplate(
    input_variables=['description_text', 'tone'],
    template='Edit this product description to be more {tone}: {description_text}. Generate a three-sentence product description with an average sentence length of 17 words. Highlight functionality and make sure to include the product name. '
)

tone_chain = LLMChain(llm=description_llm, prompt=product_description, output_key='final_description')

# setup the sequential chain
seq_chain = SequentialChain(
    chains=[description_chain, tone_chain],
    input_variables=['product_name', 'product_information', 'tone'],
    output_variables=['description_text', 'final_description'],
)

# create a function to generate the product description
def generate_product_description(product_name, product_information, tone):
    # run the chain
    result = seq_chain({'product_name': product_name, 'product_information': product_information, 'tone': tone})

    # return the final description
    return result['final_description']

def generate_product_descriptions_from_csv(csv_file_path, tone):
    # reset pointer
    if hasattr(csv_file_path, "seek"):
        csv_file_path.seek(0)
    
    # load product data from the CSV
    product_data = pd.read_csv(csv_file_path)

    # add a new column for the descriptions
    product_data['description'] = ""  

    # iterate through each row of the DataFrame
    for index, row in product_data.iterrows():
        # extract product name and information
        product_name = row['product_name']
        product_information = row['product_information']

        # generate description using the original function
        description = generate_product_description(product_name, product_information, tone)

        # store the description in the DataFrame
        product_data.loc[index, 'description'] = description 

    return product_data