from bisect import bisect
div = [i*i for i in range(1,318)]
mod = 10**9+7
def next_power_2(n): return 1 << (n-1).bit_length()
 
class segment_tree(object):
    def __init__(self, n, data):
        self.total_elements = n
        self.n = next_power_2(n) 
        self.tree = [0] * self.n + data + [0] * (self.n - n) 
 
    def build(self):
        for i in xrange(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
 
    def modify(self, pos, val):
        if pos < 0 or pos >= self.total_elements:
            print("check your inputs")
            return -1
        pos = pos + self.n
        self.tree[pos] = val
        while pos/2 > 0:
            self.tree[pos/2] = self.tree[pos] + self.tree[pos^1]
            pos = pos/2
 
    def query(self, left, right):
        if left > self.total_elements or left < 0:
            print("check your inputs")
            return -1
        if right > self.total_elements or right < 0:
            print("check your inputs")
            return -1
        left = self.n + left
        right = self.n + right
        s = 0
        while left < right:
            if left&1:
                s += self.tree[left]
                left += 1
            if right&1:
                right -= 1
                s += self.tree[right]
            left /= 2
            right /= 2
        return s
 
    def __repr__(self):
        return " ".join(str(i) for i in self.tree)
 
class Solution:
    def solve(self, A, B):
        C = []
        a = 0
        l = len(A)
        for i in xrange(l):
            p = bisect(div,A[i])
            C.append(min(div[p]-A[i],A[i]-div[p-1]))
        st = segment_tree(l, C)
        st.build()
        
        for i in xrange(len(B)):
            t,l,r = B[i]
            l-=1
            if t==1:
                p = bisect(div,r)
                st.modify(l, min(div[p]-r,r-div[p-1]))
            else: a = (a+st.query(l,r))%mod
        return a%mod
