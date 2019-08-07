nn,kk=map(int,input().split())
s=list(map(int,input().split()))
s.remove(kk)
rs=[]
for i in range(3):
    mi=abs(s[0]-kk)
    rr=s[0]
    for j in s:
        if abs(j-kk)<mi:
            rr=j
            mi=abs(j-kk)
    rs.append(rr)
    s.remove(rr)
for i in range(2):
    print(rs[i],end=" ")
print(rs[2]) 
