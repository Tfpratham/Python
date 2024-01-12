class balanceException(Exception):
    pass
class BankAccount:
    def __init__(self, initialAmount, AccName):
        self.balance=initialAmount
        self.name=AccName
        print(f"\nAccount '{self.name}' created.\nBalance = '₹{self.balance:.2f}" )

    def getBalance(self):
        print(f"\nAccount='{self.name}'.balance = '₹{self.balance:.2f}'")
        
    def Deposit(self, amount):
        self.balance = self.balance + amount
        print('\nDeposit complete.')
        self.getBalance()

    def Transation(self, amount):
        if self.balance>= amount:
            return
        else:
            raise balanceException(
                f"\n sorry , account '{self.name}' only has a balance of '₹{self.balance:.2f}'"
            )
    def Withdraw(self, amount):
        try:
            self.Transation(amount)
            self.balance = self.balance - amount
            print('\n Withdraw complete')
            self.getBalance()
        except balanceException as error:
            print(f'\n Withdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n**********STARTING THE TRANSFER')
            self.Transation(amount)
            self.Withdraw(amount)
            account.Deposit(amount)
            print('\n TRANSFER COMPLETE ✅✅**********')
        except balanceException as error:
            print(f'\n TRANSFER INTERRUPED ❌❌{error}')

# class IntrestRewardAcc(BankAccount):
#     def Deposit(self, amount):
        


       