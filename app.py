import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Initialize session state
if 'data' not in st.session_state:
    st.session_state.data = pd.DataFrame(columns=['Date', 'Category', 'Amount'])

# Upload CSV file
st.title('Personal Finance Tracker')
uploaded_file = st.file_uploader("Upload a CSV file with your financial data", type="csv")

if uploaded_file:
    st.session_state.data = pd.read_csv(uploaded_file)

# Data entry form
with st.form("expense_form"):
    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Transportation", "Entertainment", "Other"])
    amount = st.number_input("Amount", min_value=0.0)
    submitted = st.form_submit_button("Add Entry")

    if submitted:
        new_entry = pd.DataFrame([[date, category, amount]], columns=['Date', 'Category', 'Amount'])
        st.session_state.data = pd.concat([st.session_state.data, new_entry], ignore_index=True)

# Display and plot data
st.dataframe(st.session_state.data)

# Plot data
st.write("Expenses by Category")
fig, ax = plt.subplots()
st.session_state.data.groupby('Category')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%', ax=ax)
st.pyplot(fig)
