import sys
def f(): sys.stdout.flush()
n,c = map(int, input().split())
l = [30000, 10000, 2500, 500, 100]
prev = i = 0
while i<5 and n<l[i]: i+=1
start = 1
end = value = min(n, l[i])
found = False

while not(found):
    if i==5:
        for x in range(start, end+1):
            print(1,x); f()
            status = int(input())
            if status==1:
                print(3,x); f()
                found = True
                break
    else:
        print(1,value); f()
        status = int(input())
        if status==1:
            n = end
            end = value
            while i<5 and start+l[i]>=end: i+=1
            if i!=5: value = start+l[i]
            prev = 1
            print(2); f()
        else:
            start = value+1
            if prev==1:
                while i<5 and start+l[i]>=end: i+=1
                if i!=5: value = start+l[i]
            else:
                end = min(n, value+l[i])
                while i<5 and start+l[i]-1>end: i+=1
                if i!=5: value = start+l[i]-1
            prev = 0
