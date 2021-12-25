# Lonely island problem

islands, bridges, init = list(map(int, input().split()))
graph = dict()
for i in range(bridges):
    start, end = list(map(int, input().split()))
    if start not in graph:
        graph[start] = list()
    if end not in graph:
        graph[end] = list()
    graph[start].append(end)

limiting_probs = dict.fromkeys(graph.keys(), 0)

for islands in graph.values():
    if islands:
        length = len(islands)
        prob = 1 / length
        for island in islands:
            limiting_probs[island] += prob

max_val = max(limiting_probs.values())
res = [k for k, v in limiting_probs.items() if v == max_val]
print(" ".join(map(str, res)))
