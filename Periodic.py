from fractions import gcd
for numtest in range(input()):
    n = input()
    bf = map(int, raw_input().split())
    mxa = max(bf)
    s = []
    p = 0
    isok = True
    for i in range(n):
        if bf[i]>0:
            ns = i-bf[i]
            if not s: s += [ns]
            else:
                s += [ns]
                if s[-1]<s[-2]:
                    isok = False
                    break
                p = gcd(p, s[-1]-s[-2])         
    
    if isok:
        if not p: print "inf"
        else:
            if p<mxa: print "impossible"
            else: print p
    else: print "impossible"
