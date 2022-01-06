# Lonely island problem

islands, bridges, init = list(map(int, input().split()))
possible_to_get_out = False
graph = dict.fromkeys(range(1, islands + 1), 0)
for i in range(bridges):
    start, end = list(map(int, input().split()))
    if start == init:
        possible_to_get_out = True
    graph[end] += 1

if possible_to_get_out:
    print(max(graph, key=graph.get))
else:
    print(init)