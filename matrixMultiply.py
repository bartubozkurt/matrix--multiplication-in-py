X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
    # 3*3 matrix
    
Y = [[5,8,1,2],
    [6,7,3,10],
    [4,5,9,1]]
    # 3*4 matrix
    
result = [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
         # 3*4 matrix
         
# iterate through rows of X        
for i in range(len(X)):
     # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for  k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
for r in result:
    print(r)
"""    
    OUTPUT:
[114, 160, 60, 27]
[74, 97, 73, 14]
[119, 157, 112, 23]
"""
