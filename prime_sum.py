class Solution:
    def check(self, i):
        if i==2: return True
        if i<2 or i%2==0: return False
        for j in xrange(3,int(i**0.5)+2,2):
            if i%j==0: return False
        return True
        
    def solve(self, A):
        c = 0
        l = len(A)
        for i in xrange(l):
            s = 0
            for j in xrange(i,l):
                s += A[j]
                if self.check(s): c+=1
        return c
