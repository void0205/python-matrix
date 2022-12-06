def matrixformation(n):
    matrix = []
    print("Enter the values of a matrix")
    for i in range(n):
        a = []
        for j in range(n):
            a.append(int(input()))
        matrix.append(a)
    return(matrix)
def matrixprinting(matrix,n):
    print("The matrix formed is")
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end= " ")
        print()
    return matrix
def calculate(matrix):
    sd = 0
    sr = []
    sc = []
    for i in range(n):
        srsum = 0
        scsum = 0
        for j in range(n):
            if (i == j):
                sd = sd + matrix[i][j]
            srsum += matrix[i][j]
            scsum += matrix[j][i]
        sc.append(scsum)
        sr.append(srsum)
    for i in range(len(sr)):
        if (sr[i]==sc[i]==sd):
            return "Yes the sum of diagonal,row and column are same."
    return "Yes the sum of diagonal,row and column are not same"

n=int(input("Enter the dimension of the basket: "))
matrix=matrixprinting(matrixformation(n),n)
print(calculate(matrix))
