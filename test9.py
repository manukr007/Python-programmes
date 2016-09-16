#user defined function

'''
#example 1
def sample(text):
	print(text)
	return	
sample("hello")'''

'''
#example 2
def sample():
	print("hello")
	return	
sample()'''

'''
#example 3(with more than 1 parameter)
def calc(a,b):
	print("Addition",a+b)
	print("Substarction",a-b)
	return
	
calc(10,20)'''

'''#example 4 return statement
def calc(a,b):
	var=a*b
	return var
	
print(calc(10,20))'''


'''#example 5 doc screen
def func1():
	"""
This id to add 2 nos
	"""
	print(func1.__doc__)'''

	
#example 6
def add(x,y):
	sum=x+y
	return sum
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("the sum of two numbers is ",add(num1,num2))

