import streamlit as st
import requests
import json
import sys
from pprint import pprint
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('RupeeX')
st.text(" ")
st.text(" ")

url = 'https://api.apilayer.com/fixer/convert?access_key="b8Lk9wuGFpbazSoVuRVwOGYrmy9YijlG"&to=output_option&from=input_option&amount=inputnumber&result=outputnumber'
payload = {}
headers= {
  "apikey": "b8Lk9wuGFpbazSoVuRVwOGYrmy9YijlG"
}
response = requests.request("GET", url, headers=headers, data = payload)
status_code = response.status_code
result = response.text


currency_list = ['AUD', 'BGN', 'BRL', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'GBP', 'HKD', 'HRK', 'HUF', 'IDR', 'ILS','EUR','INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']
col1, col2= st.columns(2,gap="large")
with col1:
            input_option = st.selectbox('Enter current currency',(currency_list))
            st.write('Current currency : ', input_option)

            inputnumber = st.number_input('INPUT CURRENCY')
            st.write('The current value is ', inputnumber)

with col2:

            output_option = st.selectbox(
                'Converted Currency',
                (currency_list))
            st.write('Converted currency:', output_option)
            outputnumber = st.number_input('OUTPUT CURRENCY')
            st.write('The current value is ',result)




