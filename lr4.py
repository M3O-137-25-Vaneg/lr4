class Graf():
    def __init__(self):
        self.graf={}
    def sv(self,u,v):
        if u not in self.graf:
            self.graf[u]=[]
        if v not in self.graf:
            self.graf[v]=[]
        self.graf[u].append(v)
        self.graf[v].append(u)
    def versh(self):
        print("Вершины: ", list(self.graf.keys()))

def dfs(graph, start, visited):
    visited.add(start)
    print(start)
    for neighbor in graph.graf[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    ochered = [start]
    while ochered:
        posled_vershina=ochered.pop(0)
        if posled_vershina not in visited:
            print(posled_vershina,end='-')
            visited.add(posled_vershina)
            for neighbor in graph.graf[posled_vershina]:
                if neighbor not in visited:
                    ochered.append(neighbor)


g=Graf()
g.sv(0,1)
g.sv(1,2)
g.sv(2,3)
g.sv(3,4)
g.sv(4,5)
g.sv(5,6)
g.sv(6,7)
g.sv(6,8)
g.sv(6,9)
g.sv(6,10)

g.versh()
visited=set()
dfs(g, 0,visited)
bfs(g,0)