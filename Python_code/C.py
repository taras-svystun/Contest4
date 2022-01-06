# Portals problem

nplanets, nportals = list(map(int, input().split()))
prices = list(map(int, input().split()))
matrix = [[-1 for _ in range(nplanets)] for _ in range(nplanets)]
for i in range(nplanets):
    for j in range(nplanets):
        if i == j:
            matrix[i][j] = 0
        else:    
            matrix[i][j] = prices[i] + prices[j]

for k in range(nportals):
    start, end = list(map(int, input().split()))
    matrix[start - 1][end - 1], matrix[end - 1][start - 1] = 0, 0

