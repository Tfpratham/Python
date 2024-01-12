import math
#string data types 
first = 'Pratham'
last = 'Raval'

# print(type(first)) 
# print(type(first)==str)
# print(isinstance(first, str))

#concatination
fullname = first +' ' + last
print(fullname) 

fullname += ' Chirag'
print(fullname)

#casting a number to a string
introduction = " HELLO WORLD this is "+ fullname +" I am new here."
print(introduction)


#multilline
multiline = '''
hii' this is pratham chirag raval .. hii am here to learn python from scratch


'''
print(multiline)
 

 #string methods
print(first)
print(first.capitalize())
print(first.count('a'))
print(first.lower())
print(first)


# print(multiline.title())
# print(multiline.replace('hii', 'hello'))
# print(multiline)

# print(len(multiline))
# multiline += '                                     '
# multiline = '                                     '+ multiline
# print(len(multiline))

#building a menu
print('')
title = "menu".upper()
print(title.center(20, '='))
print("COFFEE".ljust(20, '.')+ '$2')
print("MUFFIN".ljust(20, '.')+ '$3')
print("TEA".ljust(20, '.')+ '$2')
print("CHEESE CAKE".ljust(20, '.')+ '$5')

print('')

#string operations
print(first[4])
print(first[-1])
print(first[2:])

#methods return boolean data 
# print(first.startswith("P"))
# print(first.endswith("P"))
# print(last.startswith("R"))
# print(last.endswith("L"))

#complex value 
comp_value = 3+5j
print(type(comp_value))
print(comp_value.real) 
print(comp_value.imag) 

#builtin math func
print(math.pi)
print(math.sqrt(81))