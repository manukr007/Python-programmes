#for loop inside list
'''num=[1,2,3,4,5,6,7,8,9]
list1=[i for i in num]
print(list1)'''

'''num=[1,2,3,4,5,6,7,8,9]
list1=[i*i for i in num]
print(list1)'''

num=[1,2,3,4,5,6,7,8,9]
list1=[i for i in num if i%2==0]
print(list1)