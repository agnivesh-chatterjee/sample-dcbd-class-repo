def matrixMult(A,B):
    for i in range(len(A)):
        for j in range(len(B[0])):
            sum = 0
            for k in range(len(B)):
                sum += A[i][k] * B[k][j]
            print(sum, end=' ')
        print()