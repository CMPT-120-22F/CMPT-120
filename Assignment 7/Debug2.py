#hi don't touch this this isn't done yet!! you can look at it though!



class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance = self.balance + amount
        return ("Successful withdrawal!")

    def deposit(self, amount):
        self.balance = self.balance + amount
        return f"Successful Deposit. Balance is now {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self, balance, interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            return f"successful transaction. Balance is {self.balance}"
        else:
            return("unable to process transaction. withdrawal would trigger overdraft limit.")

def main():
    a1 = SavingsAccount(10000,1)
    a2 = CheckingAccount(100,10)

    print(a2.withdraw(1000))
    print(a2.withdraw(10))
    print(a2.deposit(10000))
    print(a1.withdraw())


main()
