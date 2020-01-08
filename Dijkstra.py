import math
import sys

class Graph():
    def __init__(self, vertices):
        self.vert = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def dijkstra(self, graph, start, end):
        route = {}
        prev = {}
        path = []
        unvisited = graph
        infinity = sys.maxsize
        for node in unvisited:
            route[node] = infinity
        route[start] = 0

        while unvisited:
            small = None
            for node in unvisited:
                if small is None:
                    small = node
                elif route[node] < route[small]:
                    small = node

            for next, weight in graph[small].items():
                if weight + route[small] < route[next]:
                    route[next] = weight + route[small]
                    prev[next] = small
            unvisited.pop(small)

        curr = end
        while curr != start:
            try:
                path.insert(0,curr)
                curr = prev[curr]
            except KeyError:
                print('Not possible')
                break
        path.insert(0,start)
        if route[end] != infinity:
            print(str(path).replace("[","").replace("'","").replace("]",""))

def distance(lat1, lat2, long1, long2):
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)
    latdiff = lat2 - lat1
    longdiff = long2 - long1
    a = math.pow(math.sin(latdiff/2), 2) + math.cos(lat1) * math.cos (lat2) * math.pow(math.sin(longdiff/2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = 6371 * c
    return d

num = int(sys.stdin.readline().strip())
for i in range(0, num):
    count = int(sys.stdin.readline().strip())
    for k in range(0, count):
        input = {}
        k = {}
        for j in range(0, count):
            input = sys.stdin.readline().split()
            city = " ".join(input[2:])
            num1 = float(input[0])
            num2 = float(input[1])
            k[city] = num1, num2
        fuel = float(sys.stdin.readline().strip())
        dist = {}
        for city, co in k.items():
            for city2, co2 in k.items():
                if city == city2:
                    continue
                if city not in dist:
                    dist[city] = {}
                if city2 not in dist:
                    dist[city2] = {}
                if city2 in dist[city]:
                    continue
                lat1, lon1 = str(co).split(",")
                lat1, lon1 = lat1.replace("(", ""), lon1.replace(")", "").replace(" ", "")
                lat2, lon2 = str(co2).split(",")
                lat2, lon2 = lat2.replace("(", ""), lon2.replace(")", "").replace(" ", "")
                result = distance(float(lat1), float(lat2), float(lon1), float(lon2))
                if result < fuel:
                    dist[city][city2] = result
                    dist[city2][city] = result
                else:
                    dist[city][city2] = sys.maxsize
                    dist[city2][city] = sys.maxsize
        g = Graph(count)
        g.graph = dist
        start = list(dist.keys())[0]
        end = list(dist.keys())[-1]
        g.dijkstra(dist, start, end)
        try:
            count = int(sys.stdin.readline().strip())
        except:
            break
    break
