# Program to add two matrices
X = [[5,9,1],
    [3 ,8,9],
    [2 ,4,1]]
Y = [[5,1,9],
    [8,6,5],
    [4,3,2]]
result = [[0,0,0],
         [0,0,0],
         [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
for r in result:
   print(r)