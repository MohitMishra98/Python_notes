#WAP to Create Account class with 2 attributes - balance & account no. 
#Create methods for debit, credit & printing the balance.

class Account:
    def __init__(self,acc_no,bal):
        self.acc_no = acc_no
        self.bal = bal
    
    def debit(self,amt):
        self.bal-=amt
    def credit(self,amt):
        self.bal+=amt
    def show_bal(self):
        print(self.bal)

account1 = Account(989898,999999999999)

account1.show_bal()

account1.credit(9999999999)
account1.show_bal()

account1.debit(99)
account1.show_bal()