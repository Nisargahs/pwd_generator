def addpridiag(mat):
    total=0
    for i in range(len(mat)):
        total += mat[i][i]

    return total

print (addpridiag([[45,67,34],[34,4,34],[20,23,24]]))

def addsecdiag(mat):
    total=0
    for i in range(len(mat)):
        total += mat[i][len(mat)-i-1]

    return total

print (addsecdiag([[45,67],[4,34]]))