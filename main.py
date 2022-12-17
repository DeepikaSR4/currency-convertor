import streamlit as st
import requests
import json
import sys
from pprint import pprint


url = "http://data.fixer.io/api/latest?access_key=b8Lk9wuGFpbazSoVuRVwOGYrmy9YijlG"
inputcurrency = requests.get(url)
inputcurrency2 = json.loads(inputcurrency)
ix = inputcurrency2["rates"]

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('RupeeX')
<<<<<<< Updated upstream
=======
st.text(" ")
st.text(" ")
>>>>>>> Stashed changes

col1, col2= st.columns(2,gap="large")
with col1:
            input_option = st.selectbox('Enter current currency',
                ({ix}))
            st.write('Current currency : ', input_option)
            inputnumber = st.number_input('INPUT CURRENCY')
            st.write('The current value is ', inputnumber)

with col2:

            output_option = st.selectbox(
                'Converted Currency',
                ('USD', 'Rupee', 'KRW'))
            st.write('Converted currency:', output_option)
            outputnumber = st.number_input('OUTPUT CURRENCY')
            st.write('The current value is ', outputnumber)


