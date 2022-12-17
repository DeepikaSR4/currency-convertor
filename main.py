import streamlit as st


st.title('RupeeX')
<<<<<<< Updated upstream


inputnumber = st.number_input('INPUT CURRENCY')
st.write('The current value is ', inputnumber)
outputnumber = st.number_input('OUTPUT CURRENCY')
st.write('The current value is ', outputnumber)
=======
input_option = st.selectbox('Enter current currency',
    ('USD','GBP','EURO'))

st.write('Current currency : ', input_option)
>>>>>>> Stashed changes
