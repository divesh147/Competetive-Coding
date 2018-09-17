from bisect import bisect
for t in xrange(input()):
    stopy = raw_input().strip()
    stopx = raw_input().strip()
    n,m = len(stopx),len(stopy)
    winx = [0]
    winy = [0]
    losex = [0]
    losey = [0]
    for i in xrange(n):
        if stopx[i]=="0": winx.append(i+1)
        else: losex.append(i+1)
    for j in xrange(m):
        if stopy[j]=="0": winy.append(j+1)
        else: losey.append(j+1)
    
    s = ""
    for q in xrange(input()):
        i,j = map(int,raw_input().split())
        WX = bisect(winx,i)-1
        LX = bisect(losex,i)-1
        WY = bisect(winy,j)-1
        LY = bisect(losey,j)-1
        #print WX,LX,WY,LY,winx[WX],losex[LX],winy[WY],losey[LY]
        m1 = (i-winx[WX])+(j)
        m2 = (i)+(j-winy[WY])
        m3 = (i-losex[LX])+(j)
        m4 = (i)+(j-losey[LY])
        #print m1,m2,m3,m4
        ans1 = min(m1,m2)
        ans2 = min(m3,m4)
        c = "1"
        if ans1%2==0 and ans2%2: c = "0"
        s += c
    print s
