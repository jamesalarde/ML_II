import streamlit as st
import pandas as pd
from your_module import generate_product_descriptions_from_csv

def project_description():
    st.title('ML II Group Assignment')
    st.subheader('Group 8 : Joel James Alarde, Omer Althwaini, Africa Bajils Garoz, Maria do Carmo Brito e Abreu, Emiliano Puertas Ajuria')
    st.markdown('---')

    st.write("""
    
    #### :clipboard: Project Overview
    This project uses Machine Learning to generate product descriptions for e-commerce startups. The goal is to automate a portion of the startup process by generating product descriptions using AI, effectively saving time and resources.
    By using AI, high-quality product descriptions can be generated that are tailored to the specific needs of each startup, and friendly towards search engines.

    #### :hammer_and_wrench: Methodology
    The group obtained the dataset of Amazon UK products to do a style analysis and to check usual product descriptions uploaded in their online store. The dataset can be accessed here : https://www.kaggle.com/datasets/asaniczka/amazon-uk-products-dataset-2023

    The following steps were taken to create the model :
    1. Style Analysis
    2. Prompt Engineering & Validation
    3. User Interface Deployment
    
    Below is the general flow of the model.
    """)

    st.image('./ML2.png')

    st.write("""
    #### :bar_chart: Style Analysis
    The group analyzed the dataset to understand the style of product descriptions used in Amazon UK. The analysis included:
    - **Sentence Length** : the average sentence length was calculated to understand the complexity of the descriptions
    - **Tone Analysis** : the tone of the descriptions leaned towards friendly and professional, with some playful elements
    - **Functionality Highlighting** : the descriptions highlighted the functionality of the products, as this is a key aspect of effective product descriptions
             
    #### :traffic_light: Prompt Engineering & Validation
    The group used a sequential chain to generate the product descriptions.
    - The first prompt generates a three-line product description based on the product name and information.
    - The second step edits the generated description to match the selected tone.
    
    The final output is a three-sentence product description stylized to match the Amazon UK product descriptions in the dataset.
    
    #### :control_knobs: User Interface Deployment
    The group created a user interface using Streamlit to allow users to upload their own CSV files containing product names and information.
    The model generates descriptions based on the uploaded data and allows users to 1) choose their desired tone and 2) download the generated results.
    """)   

    with st.expander('Tones'):
       st.write('Friendly : Builds trust and connection with potential buyers faster and feels more personal.')
       st.write('Professional : Conveys authority and realibility.')
       st.write('Luxe : Creates a sense of exclusivity, sophistication, and elegance.')
       st.write('Playful : Makes a product more memorable, fun, and witty.')
       st.write('Minimalist : Focuses on the product itself, avoiding unnecessary details and distractions.')   

def generator_interface():
    st.write("""
    #### About the Generator
    The product description generator is designed to create high-quality product descriptions for e-commerce startups. With this app, you can upload a CSV file containing product names and information, and the model will generate a CSV file with product descriptions tailored to your needs.
    
    """)

    uploaded_file = st.file_uploader('Upload your CSV file here : ', type=['csv'])

    if uploaded_file is not None:

        tone = st.sidebar.radio('Select your preferred tone:', ['Friendly','Professional', 'Luxe', 'Playful', 'Minimalist'])

        if st.button('Generate Descriptions'):

            if uploaded_file is not None:
                result_df = generate_product_descriptions_from_csv(uploaded_file, tone)
                cleaned_df = result_df.drop(columns=['index', 'uniq_id', 'product_information'])
                st.dataframe(cleaned_df)

                csv = result_df.to_csv(index=False)
                st.download_button(
                    label='Download as CSV',
                    data=csv,
                    file_name='product_descriptions.csv',
                    mime='text/csv',
                )

                st.success('Descriptions generated successfully! Click the button above to download the CSV file.')

def meet_the_team():
    st.title("Meet the Team")
    st.write("""
    
    #### 
    Meet the team behind this amazing project! We are a group of five students from IE University.
             
    """)

    st.markdown("---")

    team_members = [
        {
            "name": "Joel James Alarde",
            "role": "Machine Learning & Data Preprocessing",
            "bio": "James focused on model training, evaluation, and cleaning the dataset to ensure the data was ready for machine learning algorithms.",
            "image": "james.jpeg"
        },
        {
            "name": "Omer Althwaini",
            "role": "Prompt Engineering",
            "bio": "Omer designed effective prompts and optimized them to improve the quality and relevance of the generated product descriptions.",
            "image": "omer.jpeg"
        },
        {
            "name": "Africa Bajils Garoz",
            "role": "Data Analysis & Visualization",
            "bio": "Africa contributed to analyzing the results and building visualizations to help interpret the model’s performance.",
            "image": "africa.jpeg"
        },
        {
            "name": "Maria do Carmo Brito e Abreu",
            "role": "Documentation & Reporting",
            "bio": "Maria was in charge of compiling project reports, writing the methodology, and ensuring the documentation was clear and complete.",
            "image": "maria.jpeg"
        },
        {
            "name": "Emiliano Puertas Ajuria",
            "role": "App Development & UI Design",
            "bio": "Emiliano developed the Streamlit user interface and integrated the model into an interactive and user-friendly web app.",
            "image": "emiliano.jpeg"
        }
    ]

    for member in team_members:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(member["image"], width=150)
        with col2:
            st.subheader(member["name"])
            st.write(f"*Role*: {member['role']}")
            st.write(member["bio"])
    st.markdown("---")

def main():
    tab1, tab2, tab3 = st.tabs(['Project Overview', 'Product Description Generator', 'Meet The Team'])
    with tab1:
        project_description()
    with tab2:
        generator_interface()
    with tab3:
        meet_the_team()

if __name__ == '__main__':
     main()