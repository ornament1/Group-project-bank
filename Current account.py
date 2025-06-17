from Account import BankAccount

class CurrentAccount(BankAccount):
    def _init_(self, holder, balance=0, overdraft_limit=1000):
        super()._init_(holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return False, f"Overdraft limit exceeded. Max allowed is ₦{self.balance + self.overdraft_limit}."
        self.balance -= amount
        return True, f"Withdrawal of ₦{amount:.2f} successful (with overdraft)."