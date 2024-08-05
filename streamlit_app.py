import streamlit as st

st.title("🏡 Property Tracker")
st.write(
    "All your Property Transactions in one Place"
)

st.header("Add New Property")

with st.form("my form"):
    address = st.text_input("Address")
    purchase_price = st.text_input("Purchase Price")
    st.form_submit_button('Submit')

st.write(address)
st.write(purchase_price)
