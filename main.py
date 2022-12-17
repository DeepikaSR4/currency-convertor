import streamlit as st


st.title('RupeeX')

input_option = st.selectbox('Enter current currency',
    ('USD','GBP','EURO'))
st.write('Current currency : ', input_option)
inputnumber = st.number_input('INPUT CURRENCY')
st.write('The current value is ', inputnumber)



outputnumber = st.number_input('OUTPUT CURRENCY')
st.write('The current value is ', outputnumber)
output_option = st.selectbox(
    'Converted Currency',
    ('USD', 'Rupee', 'KRW'))

st.write('Converted currency:', output_option)

