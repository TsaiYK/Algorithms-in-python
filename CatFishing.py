q1_head = 1;
q1_tail = 1;
q2_head = 1;
q2_tail = 1;
s_top = 0; # 桌面上牌的數量

q1_data = [0]*100; # Q1的牌
q2_data = [0]*100; # Q2的牌
s_data = [0]*10; # 桌面上的牌，用堆疊的概念
book = [0]*9; # 用來標記桌上已經有甚麼牌了

#for i in range(6):
#    q1_data[i] = input("Enter a number for Q1: ");
#    q1_tail = q1_tail + 1
q1_data[0:5] = [2,4,1,2,5,6]
q2_data[0:5] = [3,1,3,5,6,4]
q1_tail = 7;
q2_tail = 7;
    
#for i in range(6):
#    q2_data[i] = input("Enter a number for Q2: ");
#    q2_tail = q2_tail + 1
    
while q1_head<q1_tail and q2_head<q2_tail:
    t = int(q1_data[q1_head-1]) 
    # Q1先打出一張牌
    if book[t-1]==0:
        # Q1這回沒有贏牌
        q1_head = q1_head + 1
        s_top = s_top + 1
        s_data[s_top-1] = t
        book[t-1] = 1
    else:
        q1_head = q1_head + 1
        q1_data[q1_tail-1] = t
        q1_tail = q1_tail + 1
        while s_data[s_top-1] != t: 
            # 這邊使用堆疊的概念，上面的牌先拿，拿到同一個數字的那張為止
            book[s_data[s_top-1]-1] = 0
            q1_data[q1_tail-1] = s_data[s_top-1]
            q1_tail = q1_tail + 1
            s_top = s_top - 1

    t = int(q2_data[q2_head-1])
    if book[t-1]==0:
        # Q2這回沒有贏牌
        q2_head = q2_head + 1
        s_top = s_top + 1
        s_data[s_top-1] = t
        book[t-1] = 1
    else:
        q2_head = q2_head + 1
        q2_data[q2_tail-1] = t
        q2_tail = q2_tail + 1
        while s_data[s_top-1] != t:
            book[s_data[s_top-1]-1] = 0
            q2_data[q2_tail-1] = s_data[s_top-1]
            q2_tail = q2_tail + 1
            s_top = s_top - 1
    
if (q2_head==q2_tail):
    print("Q1 win")
    print("Q1 cards:",end= ' ')
    for i in range(q1_head-1,q1_tail-1):
        print(q1_data[i],end= ' ')
    if s_top>0:
        print()
        print("The cards on the table: ",end= ' ')
        for i in range(0,s_top):
            print(s_data[i],end= ' ')
    else:
        print("There in no card on the table!")

if (q1_head==q1_tail):
    print("Q2 win")
    print("Q2 cards:",end= ' ')
    for i in range(q2_head-1,q2_tail-1):
        print(q2_data[i],end= ' ')
    if s_top>0:
        print()
        print("The cards on the table: ",end= ' ')
        for i in range(0,s_top):
            print(s_data[i],end= ' ')
    else:
        print("There in no card on the table!")