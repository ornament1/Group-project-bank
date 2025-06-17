class BankAccount:
    def _init_(self, holder, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"Deposit of ₦{amount:.2f} successful."
        return False, "Deposit amount must be greater than zero."

    def get_balance(self):
        return self.balanceclass BankAccount:
    def _init_(self, holder, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True, f"Deposit of ₦{amount:.2f} successful."
        return False, "Deposit amount must be greater than zero."

    def get_balance(self):
        return self.balance