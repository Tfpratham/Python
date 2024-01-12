import math

num = int(input('enter the number you want the table of : '))
if 1<= num <=10:
    print(f'the table of the number :{num} is')
    for i in range (1,11):
        print(f"{num} * {i} ={num * i}")
    else:
        print('Enter valid number')
          