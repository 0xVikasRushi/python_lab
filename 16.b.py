def transpose(matrix):
    r= len(matrix)
    c = len(matrix[0])
    ans = [[0 for i in range(r)] for i in range(c)]
    for i in range(r):
        for j in range(c):
            ans[j][i] = matrix[i][j]
    return ans

X = [[12,7], [4 ,5],[3 ,8]]
for i in X:
    print(i)
ans = transpose(X)
for i in ans:
    print(i)