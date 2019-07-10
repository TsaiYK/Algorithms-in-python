import numpy as np

def find_repeat(source,elmt): # The source may be a list or string.
    elmt_index=[]
    s_index = 0;e_index = len(source)
    while(s_index < e_index):
        try:
            temp = source.index(elmt,s_index,e_index)
            elmt_index.append(temp)
            s_index = temp + 1
        except ValueError:
            break
    return elmt_index

Inf = 9999
n = 7
Cost = [[None]*n for i in range(n)]
#Cost = [[0,1,4,5,Inf,Inf,Inf],[1,0,Inf,2,Inf,Inf,Inf],
#        [4,Inf,0,4,Inf,3,Inf],[5,2,4,0,5,2,Inf],[Inf,Inf,Inf,5,0,Inf,6],
#        [Inf,Inf,3,2,Inf,0,4],[Inf,Inf,Inf,Inf,6,4,0]]
Cost = [[0,2,5,10,Inf,Inf,Inf],[2,0,Inf,Inf,9,Inf,Inf],
        [5,Inf,0,2,2,6,Inf],[10,Inf,2,0,Inf,3,4],[Inf,9,2,Inf,0,Inf,12],
        [Inf,Inf,6,3,Inf,0,8],[Inf,Inf,Inf,4,12,8,0]]
#Dist = [0,1,4,5,Inf,Inf,Inf]
Dist = [0,2,5,10,Inf,Inf,Inf]
Prior = [0]*n
Decided = [0]*n
Decided[0] = 1
W = [None]*n
W[0] = 0 #都是先從0開始出發
index_v = 0

while 0 in Decided:
#從0之外的第一個開始位置都是選Dist最小的節點
#先找出undecided中Dist最小的
    Undecided_index = find_repeat(Decided,0)
    min_value = Dist[Undecided_index[0]]
    for i in Undecided_index:
        if min_value>Dist[i]:
            min_value = Dist[i]
    #找到之後存到W陣列裡
    index_v = index_v + 1
    temp_index_v = Dist.index(min_value)
    if temp_index_v not in Undecided_index:
        for i in Undecided_index:
            if Dist[i]==min_value:
                W[index_v] = i
    else:
        W[index_v] = Dist.index(min_value)
    #W點的最短距離已決定
    Decided[W[index_v]] = 1
    #檢查W身邊的點的Dist是否變近
    b = np.arange(n)
    b2 = b[np.array(Cost[W[index_v]])<Inf]
    neighbour = [None]*(len(b2)-1)
    j=0
    for i in range(len(b2)):
        if Cost[W[index_v]][b2[i]]!=0:
            neighbour[j] = b2[i]
            j=j+1
    for i in neighbour:
        if Dist[i]>Dist[W[index_v]]+Cost[W[index_v]][i]:
            Dist[i] = Dist[W[index_v]]+Cost[W[index_v]][i]
            Prior[i] = W[index_v]
            
