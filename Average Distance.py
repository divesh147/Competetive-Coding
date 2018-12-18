# Python 2
t=int(raw_input())
for _ in range(t):
    n,m=[int(x) for x in raw_input().split()]
    k=n+m
    a=[]
    for i in range(n):
        a.append(raw_input())
    ans=[0]*k

    for i in range(n):
        tmp=[0]*k
        for j in range(m):
            ans1=[0,0]
            ans1.extend(tmp[1:-1])
            if j>0 and a[i][j-1]=="1":
                ans1[1]=1
            
            for x in range(i+1,n):
                if a[x][j]=="1":
                    ans1[abs(x-i)]+=1

            if a[i][j]=="1":
                for x in range(k-1):
                    ans[x]+=ans1[x]

            for x in range(i):
                if a[x][j]=="1":
                    ans1[abs(x-i)]+=1

            tmp=ans1[:]

    for i in range(1,k-2):
        print ans[i],
    print ans[k-2]
            
                    
    
