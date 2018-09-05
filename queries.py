mod = 10**9+7
class Solution:
    def prod(self, n):
        p = 1
        for i in xrange(1, int(n**0.5 + 1)):
            if n%i==0:
                if n/i==i: p = (p*i)%mod
                else:
                    p = (p*i)%mod
                    p = (p*(n/i))%mod
        return p%mod
 
    def solve(self, A, B):
        n = len(A)
        left = [1 for i in xrange(n)]
        right = [1 for i in xrange(n)]
        
        for i in xrange(1,n):
            prev = i-1
            while prev>=0 and A[i]>A[prev]:
                left[i] += left[prev]
                prev -= left[prev]
        
        for i in xrange(n-2,-1,-1):
            nex = i+1
            while nex<n and A[i]>=A[nex]:
                right[i] += right[nex]
                nex += right[nex]
        
        d = [left[i]*right[i] for i in xrange(n)]
        p = [self.prod(A[i]) for i in xrange(n)]
        
        z = zip(p,d)
        z.sort(reverse=True)
        s = 0
        d = []
        p = []
        for i in xrange(n):
            p.append(z[i][0])
            d.append(s+z[i][1])
            s += z[i][1]
        
        x = []
        for i in xrange(len(B)):
            k = B[i]
            low = 0
            high =  n
            pos = -1
            if k<=d[0]: pos = 0
            if pos==-1:
                while low<=high:
                    mid = (low+high)/2
                    if d[mid]<k and k<=d[mid+1]:
                        pos = mid+1
                        break
                    elif d[mid]<k: low = mid+1
                    else: high = mid-1
            x.append(p[pos])
        return x
