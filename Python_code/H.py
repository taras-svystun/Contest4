# Dividing the graph problem

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))

minimal, cheapest = 10000000, 0
for idx, vertex in enumerate(graph):
    edges = vertex.count(1)
    if edges < minimal:
        minimal, cheapest = edges, idx + 1
    
rest = [i for i in range(1, n + 1) if i != cheapest]
print(cheapest)
print(" ".join(map(str, rest)))