class Queue:
    def __init__(self,x,y,f,s):
        self.x = x
        self.y = y
        self.f = f
        self.s = s

m = 5 # row
n = 4 # column

a = [[None]*n for i in range(m)]
book = [[None]*n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = 0
        book[i][j] = 0
a[0][2] = 1
a[2][2] = 1
a[3][1] = 1
a[4][3] = 1
head = 0
tail = 0
startx = 0
starty = 0
p = 2
q = 3
que = [None]*2500
que[tail] = Queue(startx,starty,0,0)
tail = tail + 1
book[starty][startx] = 1
path_next = [[-1,0],[1,0],[0,-1],[0,1]] # left,right,up,down

flag = 0

while head<tail:
    for i in range(4):
        tx = que[head].x + path_next[i][0]
        ty = que[head].y + path_next[i][1]
        if ty<0 or ty>=m or tx<0 or tx>=n:
            continue
        if a[ty][tx]==0 and book[ty][tx]==0:
            book[ty][tx] = 1
            que[tail] = Queue(tx,ty,head,que[tail-1].s+1)
#            que[tail].x = tx
#            que[tail].y = ty
#            que[tail].f = head
#            que[tail].s = que[head].s + 1
            tail = tail + 1
        if tx==q and ty==p:
            flag = 1
            break
    if flag == 1:
        break
    head = head + 1
print(que[tail-1].s)