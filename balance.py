class Balance:
    def __init__(self,balance,accountno):
        self.balance=balance
        self.accountno=accountno
    def credit(self,amount):
        self.balance=self.balance+amount
        print(amount,"credited")
    def debit(self,amount):
        if amount<=self.balance:
            self.balance=self.balance-amount
            print(amount,"debited")
        else:
            print("Insufficient balance!")
    def print_balance(self):
        print("Accountno", self.accountno)
        print("Balance", self.balance)

acc1=Balance(345,"75678907890")
acc1.credit(6700)
acc1.debit(500)
acc1.print_balance()
        
