c = int(input("Initial Loan: "))
n = int(input("Years of the loan: "))
i = float(input("Annual Interest rate: "))

ii = i/100

x = c * ii * (1 + ii) ** n 

y = (1 + ii) ** n - 1

Annual = x / y

Monthly = Annual / 12

print("The annual payment is %s" %(Annual))

print("The monthly payment is %s" %(Monthly))