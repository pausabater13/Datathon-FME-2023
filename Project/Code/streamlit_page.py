import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_icon=":chart_with_upwards_trend:",
    layout="wide",  # Puedes cambiar a "centered" o "wide"
    initial_sidebar_state="expanded",  # Puedes cambiar a "collapsed"expanded
    )

# Load the dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
#df = pd.read_csv('your_dataset.csv')

# Streamlit web app
def main():
    st.title("Fashion Compatibility Challenge - Datathon 2023")

    col1,col3, col2 = st.columns(3)

    # Display input boxes for each parameter

    image_path = os.path.join('..','Data', 'mango_logo.png')
    col1.image(image_path, use_column_width=True)#caption='Generated Image',
    cod_modelo_color = col1.text_input("Identifier for fashion product based on model & color.", "")
    num_clothes_per_outfit = col1.text_input("Number of clothes per outfit. Default: arbitrary.", "")

    col3, col4 = st.columns(2)

    # Submit button
    if col1.button("Submit"):
        logo_path = os.path.join('../../datathon-2023-fashion-compatibility-main/datathon/dataset/images', cod_modelo_color.replace("-","_")+".jpg")
        if logo_path:
            col2.image(logo_path,  use_column_width="auto") #'''caption='Generated Image','''
        else:
            col2.warning("No matching logo_image found.")
    
    # Add content to the new columns
    col3.write("Column 4 content")
    col4.write("Column 5 content")

    
    

if __name__ == '__main__':
    main()
