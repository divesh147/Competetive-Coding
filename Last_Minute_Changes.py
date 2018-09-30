class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        l = len(A)
        k = A[l/2]
        ksum = 0
        for i in xrange(l): ksum += abs(A[i]-k)
        return ksum
