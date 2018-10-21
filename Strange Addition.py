def solve(a, b, c):
    if a == 0: return bin(c).count('1') == b
    if b == 0: return bin(c).count('1') == a
    if c < 0 : return 0
    if c == 0: return a == b and a == 0
    if (a, b, c) in d: return d[(a, b, c)]
    
    if c&1: x = solve(a-1, b, c >> 1) + solve(a, b-1, c >> 1)
    else: x = solve(a, b, c >> 1) + solve(a-1, b-1, (c >> 1)-1)
    d[(a, b, c)] = x
    return x

d = {}
for _ in xrange(input()):
    a, b, c = map(int, raw_input().split())
    print solve(bin(a).count('1'), bin(b).count('1'), c)
