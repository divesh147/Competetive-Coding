from bisect import bisect
mod = 10**9+7
prime = [2,3]
for i in xrange(5,10**6+15,2):
    f = 1
    for j in xrange(1,bisect(prime, int(i**0.5+1))):
        if i%prime[j]==0:
            f = 0
            break
    if f: prime.append(i)

def summ(n): return pow(2,n)-1

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        nx = c = t = 0
        for j in xrange(len(A)):
            if A[j]!=1: break
        for i in xrange(j,len(A)):
            if A[i]<prime[nx]: t+=1
            else:
                c = (c + summ(t))%mod
                t = 1
                while A[i]>=prime[nx]: nx+=1
        c = (c + summ(t))%mod
        return c%mod
