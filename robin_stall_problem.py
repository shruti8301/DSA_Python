n=int(input("Enter the value of N"))
m=int(input("Enter the no of stalls"))
a=[]
d=[]
query=[]
co=[]
for i in range(0,m):
    b=[]
    for j in range(0,10):
        b.append(int(input("Enter the stalls m accepting j")))
    a.append(b)
    print(a)
for k in range(0,n):
    c=[]
    for l in range(0,10):
        c.append(int(input("Enter the persons i has coupons j")))
    d.append(c)
q=int(input("Enter the number of queries"))
for o in range(0,q):
    e=[]
    for n in range(0,2):
        e.append(int(input("sets of queries")))
    query.append(e)
    print(query)
    
#logic ------------------------
    
for i in range (len(a)):
    for j in range(len(a[i])):
        if(a[i][j]==1):
            print(i+1,j+1)
            stall_no=i+1
            coupon_accept=j+1
for k in range (len(d)):
    for l in range(len(d[k])):
        if(d[k][l]==1):
            print(k+1,l+1)
            person_no=k+1
            person_coupon=l+1

for p in range (len(query)):
    for q in range(len(query[p])):
        bhd=query[p][0]
        print(bhd)
        if(bhd==stall_no):
            for i in range (len(a)):
                for j in range(len(a[i])):
                    if (query[p][1]==a[(stall_no - 1)][j]):
                        co.append(1)
                    else:
                        co.append(0)

            print(co)
       

            
    
                

            
            
