weight =float(input("Enter the weight of the package in kilogram: "))
distance = int(input("Enter the distance on kilometers: "))

if weight <= 0 and distance <= 0 :
    print('Enter valid weight and distance: ')
elif weight <= 2:
    cost = 80 * distance
elif weight <= 6:
    cost = 100 * distance
elif weight <= 8 :
    cost = 120 * distance
elif weight == 10:
    cost = 150 * distance 
else:
    cost = 150 * distance

print(f'\n the cost of your delivery is : {int(cost)}')