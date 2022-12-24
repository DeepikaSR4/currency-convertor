import streamlit as st
import requests

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

st.title('RupeeX')
st.text(" ")
st.text(" ")


currency_list = ['AUD', ' BGN', ' BRL', ' CAD', ' CHF', ' CNY', ' CZK', ' DKK', ' GBP', ' HKD', 'HRK', 'HUF', 'IDR', 'ILS','EUR','INR', 'ISK', 'JPY', 'KRW', 'MXN', 'MYR', 'NOK', 'NZD', 'PHP', 'PLN', 'RON', 'RUB', 'SEK', 'SGD', 'THB', 'TRY', 'USD', 'ZAR']





col1, col2,col3= st.columns(3,gap="large")
with col1:
            input_option= st.selectbox('Enter current currency',
["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYN","BYR","BZD","CAD","CDF","CHF","CLF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","LVL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPF","YER","ZAR","ZMK","ZMW","ZWL"])
            st.write('Current currency : ',input_option)

          

with col2:
            inputnumber = st.number_input("INPUT AMOUNT",value=1.00)
            
with col3:
          output_option = st.selectbox('Converted Currency',
["AED","AFN","ALL","AMD","ANG","AOA","ARS","AUD","AWG","AZN","BAM","BBD","BDT","BGN","BHD","BIF","BMD","BND","BOB","BRL","BSD","BTC","BTN","BWP","BYN","BYR","BZD","CAD","CDF","CHF","CLF","CLP","CNY","COP","CRC","CUC","CUP","CVE","CZK","DJF","DKK","DOP","DZD","EGP","ERN","ETB","EUR","FJD","FKP","GBP","GEL","GGP","GHS","GIP","GMD","GNF","GTQ","GYD","HKD","HNL","HRK","HTG","HUF","IDR","ILS","IMP","INR","IQD","IRR","ISK","JEP","JMD","JOD","JPY","KES","KGS","KHR","KMF","KPW","KRW","KWD","KYD","KZT","LAK","LBP","LKR","LRD","LSL","LTL","LVL","LYD","MAD","MDL","MGA","MKD","MMK","MNT","MOP","MRO","MUR","MVR","MWK","MXN","MYR","MZN","NAD","NGN","NIO","NOK","NPR","NZD","OMR","PAB","PEN","PGK","PHP","PKR","PLN","PYG","QAR","RON","RSD","RUB","RWF","SAR","SBD","SCR","SDG","SEK","SGD","SHP","SLL","SOS","SRD","STD","SVC","SYP","SZL","THB","TJS","TMT","TND","TOP","TRY","TTD","TWD","TZS","UAH","UGX","USD","UYU","UZS","VEF","VND","VUV","WST","XAF","XAG","XAU","XCD","XDR","XOF","XPF","YER","ZAR","ZMK","ZMW","ZWL"])
          st.write('Converted currency:', output_option)


url = "https://currency-conversion-and-exchange-rates.p.rapidapi.com/convert"

querystring = {
  "from":input_option,
  "to":output_option,
  "amount":inputnumber
  }

headers = {
	"X-RapidAPI-Key": "50433c2987msh40a9b38598b4f4bp183a24jsnc259adef6df4",
	"X-RapidAPI-Host": "currency-conversion-and-exchange-rates.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
if response.status_code == 200:

      data = response.json()
      print(data)
      result = data['result']
      

if result!=0:
  col1, col2,col3= st.columns(3,gap="large")
  with col1:
      st.write('')
  with col2:
      st.write('The current value is ',result)
  with col3:
      st.write('')
    
else:
  col1, col2,col3= st.columns(3,gap="large")
  with col1:
      st.write('')
  with col2:
      st.write('The input value cannot be null')
  with col3:
      st.write('')




st.write('')
st.write('')
st.write('')

st.write('Made by LUNE')








