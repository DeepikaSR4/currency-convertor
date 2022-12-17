import streamlit as st


st.title('RupeeX')


inputnumber = st.number_input('INPUT CURRENCY')
st.write('The current value is ', inputnumber)
outputnumber = st.number_input('OUTPUT CURRENCY')
st.write('The current value is ', outputnumber)
