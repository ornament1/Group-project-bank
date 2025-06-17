import streamlit as st
from SavingsAccount import SavingsAccount
from CurrentAccount import CurrentAccount

def main():
    st.title("💳 Bank App")
    account_type = st.selectbox("Select account type", ["Savings", "Current"])

    if account_type == "Savings":
        account = SavingsAccount("User", 1000)
    else:
        account = CurrentAccount("User", 1000)

    st.write(f"💰 Balance: ₦{account.get_balance():.2f}")

    amount = st.number_input("Enter amount", min_value=0)

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Deposit"):
            success, message = account.deposit(amount)
            if success:
                st.success(message)
            else:
                st.error(message)
    with col2:
        if st.button("Withdraw"):
            success, message = account.withdraw(amount)
            if success:
                st.success(message)
            else:
                st.error(message)

    st.write(f"💰 Updated balance: ₦{account.get_balance():.2f}")

if _name_ == "_main_":
    main()