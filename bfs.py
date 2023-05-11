graph={"A":["B","C"],
       "B":["A","C","D"],
       "C":["A","B","E","F"],
       "D":["B","E"],
       "E":["C","D","G"],
       "F":["C","G"],
       "G":["E","F"]}
stack=[]
vis=[]
p=[]
def dfs(vertex,graph,stack,vis):
    
queue=[]
vis=[]
def bfs(vertex,graph,queue,vis):
    queue.append(vertex)
    vis.append(vertex)
    while queue:
        ele=queue.pop(0)
        for i in graph[ele]:
            if i not in vis:
                queue.append(i)
                vis.append(i)
bfs("G",graph,queue,vis)
print(vis)

