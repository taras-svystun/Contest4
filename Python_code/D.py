# Chicago 106 problem
# try https://e-maxx.ru/algo/levit_algorithm

places, streets = list(map(int, input().split()))
graph = dict()
# dynamic = [-1 for i in range(places)]
for i in range(streets):
    start, end, prob = list(map(int, input().split()))
    if start not in graph:
        graph[start] = list()
    if end not in graph:
        graph[end] = list()
    graph[start].append(end)
    graph[end].append(start)


