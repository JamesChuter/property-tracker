import streamlit as st

st.title("🏡 Property Tracker")
st.write(
    "All your Property Transactions in one Place"
)

st.header("Add New Property")

with st.form("my form"):
    st.text_input("Address")
    st.text_input("Purchase Price")
    st.form_submit_button('Submit')
