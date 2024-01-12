#methods of list 
users = ['Pratham', 'bhavin','bobby','Krish']
data = ['fuizail','nelson','Rahul']
print(users)

print(len(users))

#methods to add more items to the list
users.append('dhairya')
print(users)

#i this method dont forget to add '' 
users += ['shashank']
print(users)

users.extend(['febin','smith'])
print(users)

# users.extend(data)
# print(users)

users[3:2]=['reubn','yohaan'] 
print(users)

#removing data from the list
users.remove('reubn')
print(users)

del users[1]
print(users)

#sorting the list
#key is used to include lower cased alphabets to be in sorted order 
users.sort(key=str.lower)
print(users)

nums = [6,7,1,4,2,3,9,8,5]
nums.reverse()
print(nums)


nums.sort(reverse=True)
print(nums)

#tuples bhi hai..can easlity learn from any website

