def dfs(x,y,step):
    global min_value, p, q, num
    path_next = [[-1,0],[1,0],[0,-1],[0,1]] # left,right,up,down
    if x==q and y==p:
        if step<min_value:
            min_value = step
        return
    for k in range(4):
        tx = x + path_next[k][0]
        ty = y + path_next[k][1]
#        print(tx)
#        print(ty)
#        print()
        if ty<0 or ty>=m or tx<0 or tx>=n:
#            num = num + 1
            continue
        if a[ty][tx]==0 and book[ty][tx]==0:
            book[ty][tx] = 1
            dfs(tx,ty,step+1)
            book[ty][tx] = 0
    
m = 8#5 # row
n = 7#4 # column
min_value = 9999
#num = 0

a = [ [None] * n for i in range(m) ]
book = [ [None] * n for i in range(m) ]
for i in range(m):
    for j in range(n):
        a[i][j] = 0
        book[i][j] = 0
#a[0][2] = 1
#a[2][2] = 1
#a[3][1] = 1
#a[4][3] = 1
a[1][1] = 1
a[2][1] = 1
a[5][0] = 1
a[2][2] = 1
a[6][2] = 1
a[5][3] = 1
a[5][4] = 1
a[2][5] = 1
a[4][5] = 1

for i in range(m):
    for j in range(n):
        print(a[i][j],end='')
    print()
    
#print()
#for i in range(m):
#    for j in range(n):
#        print(book[i][j],end='')
#    print()

#startx = int(print("Please enter the initial x-coordinate of you: "))
#starty = int(print("Please enter the initial y-coordinate of you: "))
startx = 0
starty = 0
book[startx][starty] = 1
p = 6#2
q = 3#3
#p = int(print("Please enter the x-coordinate of the man saved: "))
#q = int(print("Please enter the y-coordinate of the man saved: "))
dfs(startx,starty,0)
print("The minimum of steps is: ",min_value)





    


