from Account import BankAccount

class SavingsAccount(BankAccount):
    def _init_(self, holder, balance=0, withdrawal_limit=500):
        super()._init_(holder, balance)
        self.withdrawal_limit = withdrawal_limit

    def withdraw(self, amount):
        if amount > self.withdrawal_limit:
            return False, f"Cannot withdraw above ₦{self.withdrawal_limit} in Savings Account."
        if amount <= self.balance:
            self.balance -= amount
            return True, f"Withdrawal of ₦{amount:.2f} successful."
        return False, "Insufficient balance."