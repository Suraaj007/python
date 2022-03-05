class Account():
    def __init__(self,owner,balance=0):
        self.owner= owner
        self.balance= balance

    def deposits(self,dep_amt):
        self.balance=self.balance+ dep_amt    
        print(f'added {dep_amt} to the balance')
    def withdrawal(self,wd_amt):
        if self.balance>=wd_amt:
            self.balance=self.balance-wd_amt
            print('withdrawal accepted')
        else:
            print('sorry not enough funds!')
    def __str__(self) -> str:
        return f'owner is {self.owner} \nbalance: {self.balance} '            
a= Account ('sam',500)
print(a.balance)       
print(a.owner)
a.deposits(100)
print(a)
a.withdrawal(600)
a.withdrawal(1)

