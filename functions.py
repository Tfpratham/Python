# #def is a reserved keyword
# def greethello(name , thankyou ):
#     print('HEllo WOrld ' + name)
#     print('HEllo WOrld ' + thankyou)
#     print('HEllo WOrld')
#     print(thankyou)
# def letterhai_bhai(naam , tareek):
#     st = f"hi maam mera naam {naam} hai aur mei {tareek} ko nahi aaunga "
#     print(st)

# def average(a,b):
#     return(a+b/2)
# greethello('Pratham', 'Rutuja')
# letterhai_bhai("Pratham", '2january')
# letterhai_bhai("Rutuja", '3january')
# print(average(1000,2000))

import math
def rect_area(length, breadth):
    return length * breadth
    
def circle_area(radius):
    return math.pi *radius*radius

def square_area(side):
    return side*side 

rect_len=5
rect_bre=5
num_rad=3
num_side=7

print(f'area of rect  is : {rect_area(rect_len, rect_bre)}')
print(f'area of circle  is: {circle_area(num_rad)}')
print(f'area of square  is: {square_area(num_side)}')
