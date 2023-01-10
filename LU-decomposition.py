# LU-decomposition project
# by saba sarmadi 400442171 and amirabbas gashtil 400442333 
MAX = 100

def luDecomposition(mat, n):
    lower = [[0 for x in range(n)]  
        for y in range(n)]
    upper = [[0 for x in range(n)]
        for y in range(n)]

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

                upper[i][k] = mat[i][k] - sum
                for k in range(i, n):
                    if (i == k):
                        lower[i][i] = 1 

                    else:
                        sum = 0
                        for j in range(i):
                            sum += (lower[k][j] * upper[j][i])
                            lower[k][i] = int((mat[k][i] - sum) / upper[i][i])

if __name__ == "__main":
    pass
