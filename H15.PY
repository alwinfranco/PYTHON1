m=int(input())
l=list(map(int, input().split()))[:m]
mx=max(l)
fml=[]
for i in range(0,len(l)):
    new=l[i:]
    fi=max(new)
    if(l[i]==fi):
        fml.append(l[i])
print(*fml)
print(mx)
