def preference_compare(EngagedMan,ProposedMan,w_preference):
    #比較女生現在訂婚的對象和跟她求婚的對象哪個比較好
    #若求婚的對象優於訂婚對象，則輸出1；否則輸出0
    if w_preference.index(ProposedMan) < w_preference.index(EngagedMan):
        return 1
    else:
        return 0

ManPref = []
WomanPref = []
ManPref = [[4,2,3,1,5],[5,3,2,1,4],[2,5,1,4,3],[5,2,4,3,1],[4,1,2,3,5]]
WomanPref = [[4,2,5,3,1],[2,1,4,3,5],[1,3,5,4,2],[4,1,3,2,5],[2,5,1,3,4]]
# Initially all m ∈ M and w ∈W are free
man = [None]*6
ManFree = [1,1,1,1,1]
ManNextPropose = [1,1,1,1,1]
EngagedWoman = [0,0,0,0,0]
num = 0
        

while(ManFree.count(1)!=0):
    num += 1
    # Choose such a man m
    m = ManFree.index(1)+1
    w = ManPref[m-1][ManNextPropose[m-1]-1] # w is the highest-ranked woman in m's preference
    if EngagedWoman[w-1] == 0:
        EngagedWoman[w-1] = m
        ManFree[m-1] = 0
        ManNextPropose[m-1] += 1
    else:
        if preference_compare(EngagedWoman[w-1],m,WomanPref[w-1]) == 1: # Proposed is better
            
            ManFree[m-1] = 0
            #把成功訂婚的人從失戀陣線聯盟移除
            
            ManFree[EngagedWoman[w-1]-1] = 1
            #把這個原本已經訂婚但是被淘汰的男生放回去失戀陣線聯盟
            
            EngagedWoman[w-1] = m
            #取代原本已經訂婚的人，改為propose的那個男生
            
            ManNextPropose[m-1] += 1
        else:
            ManNextPropose[m-1] += 1
            continue
                
print(EngagedWoman)