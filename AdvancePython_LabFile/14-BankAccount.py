# 14- Create a BankAccount class. Your class should support the following methods: 
# a. __init__(self, account_no) 
# b. deposit (self, account_no, amount) 
# c. withdraw (self, account_no, amount) 
# d. get_balance (self, account_no)

class BankAccount:
    def __init__(self,accNo) -> None:
        self.accNo=accNo
        self.balance=0
    def deposit(self, amount):
        self.balance=self.balance+amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
        else:
            print("You don't have sufficient balance")
    def getBalance(self):
        print("Your Account Number: ",self.accNo)
        print("Your total balance = ",self.balance)

if __name__=='__main__':
    acc=input("Enter your account number")
    ba=BankAccount(acc)
    ba.getBalance()

    dep=int(input("Enter the amount to be deposited"))
    ba.deposit(dep)
    ba.getBalance()

    wid=int(input("Enter the amount to be withdrawl"))
    ba.withdraw(wid)
    ba.getBalance()