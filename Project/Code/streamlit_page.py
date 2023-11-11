import streamlit as st
import pandas as pd
import os

# Load the dataset
# Replace 'your_dataset.csv' with the actual path to your dataset
#df = pd.read_csv('your_dataset.csv')


# Streamlit web app
def main():
    st.title("Clothing Image Viewer")

    col1, col2, col3 = st.columns(3)

    # Display input boxes for each parameter
    cod_modelo_color = col1.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    cod_color_code = col1.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    des_color_specification_esp = col1.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    des_agrup_color_eng = col1.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))

    des_sex = col2.selectbox("cod_modelo_color",("Unisex", "Female", "Male"))
    des_age = col2.selectbox("cod_modelo_color",('Kids', 'Adult'))
    des_line = col2.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    des_fabric = col2.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))

    des_product_category = col3.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    des_product_aggregated_family = col3.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    des_product_family = col3.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))
    des_product_type = col3.selectbox("cod_modelo_color",('Email', 'Home phone', 'Mobile phone'))

    # Submit button
    if st.button("Submit"):
        image_path = os.path.join('..','Data', 'mango_logo.png')
    
        if image_path:
            st.image(image_path, caption='Generated Image', use_column_width=True)
        else:
            st.warning("No matching image found.")
    else:
        image_path = os.path.join('..','Data', 'mango_logo.png')
        st.image(image_path, caption='Generated Image', use_column_width=True)

if __name__ == '__main__':
    main()
