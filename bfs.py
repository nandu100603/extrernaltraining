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

    
info
abstract
intro
existing sol
proposed sol
tools or softwares
references





22 60 le3
09 15 45
38 b7
12 17 37
54 24 11

A1 55 5800000000000








b1   40 36 46
b2   61 92 90
b3   39 01 A7
b4   64 b9 89
b5   71 23 c1
.b6   le10 le08 A8
b7   35 83 le12
.b8   59 86 A0
.b9   32 le9 28
.b10  10 72 A9
b11  18 81 70
b12  84 76 75
b13  74 44 25
b14  62 43 96
.b15  b2 77 88
b16  22 60 le3
b17  09 15 45
b18  12 17 37
b19  54 24 11
b20 03 le02 56


Actually existing solution lo max pooling technique 2 times and conventional layer 1 time use chesaru
proposed solution lo maxpolling 3 times and conventional layer 2 times use chesdam ok
dhini valla manaki image size thagguthundhi features more extract avvuthay and
inka size of data sets thagguthundhi inka efficiency thagguthundhi
and relu activation function vadaru so dhani badhulu tanhx vaduthamu
because relu overfitting avvuthundhi tanhx perfect fitting avvuthundhi
then the learning point will shif from local maxima to global maxima





max pooling 2times layerd okkati convential layer
3 2 functuin relu tanhx activation function
image size thagghundhi fetures more extract avvuthay inka size thaggundhi effinciency peruguthundhu
relu ovvarfit tanhx anedhi perfect fit 
min polling



training sigmoid or tanhx it can reduce the local global maximum
the learning point shift from local maxima to global maxima

draw backs


