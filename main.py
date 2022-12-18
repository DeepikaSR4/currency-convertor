import streamlit as st
import requests

from pprint import pprint
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('RupeeX')
st.text(" ")
st.text(" ")

currency_list = ['AUD', ' BGN', ' BRL', ' CAD', ' CHF', ' CNY', ' CZK', ' DKK', ' GBP', ' HKD', 'HRK', 'HUF', 'IDR', 'ILS','EUR','INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']


url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

#querystring = {'from': 'input_option','to': 'output_option','amount':'inputnumber'}
querystring = {'from': 'USD','to': 'INR','amount':'1'}
headers = {
	"X-RapidAPI-Key": "50433c2987msh40a9b38598b4f4bp183a24jsnc259adef6df4",
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
} 

response = requests.request("GET", url, headers=headers, params=querystring)
output = response.json()
result = (output['result'])
print(result)


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

  

st.write('')
st.write('Made by LUNE')






