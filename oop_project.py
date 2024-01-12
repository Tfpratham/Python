from bank_account import *

Chirag = BankAccount(9000, 'Chirag')
Hema = BankAccount(7000, 'Hema')
Pratham = BankAccount(5000, 'Pratham')
Rutuja = BankAccount(3000, 'Rutu')

Pratham.getBalance()
Rutuja.getBalance()

Rutuja.Deposit(1000)

Pratham.Withdraw(50000)
Pratham.Withdraw(500)

Chirag.transfer(10000 , Pratham)
Chirag.transfer(1000 , Pratham)