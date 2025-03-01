def adddiag(mat):
    total1=0
    total2=0
    for i in range(len(mat)):
        total += mat[i][i]
        total += mat[i][len(mat)-i-1]

    return total1
    return total2 
print (adddiag([[45,67,34],[34,4,34],[20,23,24]]))


#whether a string can be palindromable or not 