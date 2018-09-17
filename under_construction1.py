def check(n):
    x = n**0.5
    return pow(int(x),2)==pow(x,2)

class segment_tree(object):
    def __init__(self, n, data):
        self.total_elements = n
        self.n = 1<<(n-1).bit_length() # next power of 2 >= n
        self.tree = [0] * self.n + data + [0] * (self.n - n) 
 
    def build(self):
        for i in xrange(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] & self.tree[2*i+1]

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

for t in xrange(input()):
    n,q = map(int,raw_input().split())
    a = map(int,raw_input().split())
    st = segment_tree(n,a)
    st.build()
    for _ in xrange(q):
        l,r = map(int,raw_input().split())
        print st.query(l,r)
st.build()
st.query(l,r)
A = [i*2 for i in xrange(10**4)]
C = []
l = len(A)
for i in xrange(l):
    p = bisect(div,A[i])
    C.append(min(div[p]-A[i],A[i]-div[p-1]))
st = segment_tree(l, C)
st.build()
st.query(l,r)
