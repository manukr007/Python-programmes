#for loop example
'''list1=['hello','world']
for i in list1:
	for j in i:
		print(j)'''
		
'''list1=[]
for letter in 'abcd':
	for num in range(4):
		list1.append((letter,num))
print(list1)'''


list1=[(letter,num) for letter in 'abcd' for num in range(4)]
print (list1)
