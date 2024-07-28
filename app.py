import streamlit as st
import pandas as pd
import plotly.express as px

# Initialize session state if it doesn't exist
if 'transactions' not in st.session_state:
    st.session_state.transactions = pd.DataFrame(columns=['Date', 'Type', 'Category', 'Amount', 'Description'])

def add_transaction(date, transaction_type, category, amount, description):
    new_transaction = pd.DataFrame([[date, transaction_type, category, amount, description]], columns=['Date', 'Type', 'Category', 'Amount', 'Description'])
    st.session_state.transactions = pd.concat([st.session_state.transactions, new_transaction], ignore_index=True)

def plot_data():
    df = st.session_state.transactions
    
    if not df.empty:
        # Plot by Type
        st.header('Expenses and Incomes Overview')
        fig = px.bar(df, x='Date', y='Amount', color='Type', title='Expenses and Incomes by Date')
        st.plotly_chart(fig)

        # Plot by Category
        st.header('Expenses and Incomes by Category')
        fig_cat = px.pie(df, names='Category', values='Amount', color='Type', title='Distribution by Category')
        st.plotly_chart(fig_cat)

def main():
    st.title('Finance Tracker')

    # Form to add new transactions (both expenses and incomes)
    with st.form(key='transaction_form'):
        st.header('Add New Transaction')
        date = st.date_input('Date')
        transaction_type = st.selectbox('Transaction Type', ['Expense', 'Income'])
        category = st.selectbox('Category', ['Food', 'Transport', 'Entertainment', 'Others'])
        amount = st.number_input('Amount', min_value=0.01, format="%.2f")
        description = st.text_input('Description')

        submit_button = st.form_submit_button(label='Add Transaction')
        if submit_button:
            add_transaction(date, transaction_type, category, amount, description)
            st.success('Transaction added successfully!')

    # Display transactions
    st.header('Transactions Summary')
    st.dataframe(st.session_state.transactions)

    # Plot data
    plot_data()

    # Export to CSV
    if st.button('Export to CSV'):
        csv = st.session_state.transactions.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name='transactions.csv',
            mime='text/csv'
        )

if __name__ == "__main__":
    main()
