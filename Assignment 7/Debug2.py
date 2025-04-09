class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance + amount
        return ("Successful withdrawal!")

    def deposit(self, amount):
        #how would you add the amount to the current balance?
        return f"Successful Deposit. Balance is now {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        #call the super init here, passing in balance as the parameter.
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate
        return("Interest applied to this account.")

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            return f"successful transaction. Balance is {self.balance}"
        else:
            #if we're hitting this else, what happened? What should you tell the user?
            return("?")

def main():
    #create a savings account and a checking account with a deposit of $100. Set the interest rate to be .2, set the overdraft limit to be 10.

    #apply interest to the savings account

    #withdraw $50 from the checking account.
    
    #withdraw $100 from the checking account.
    
    #display the balance of each account.

main()
