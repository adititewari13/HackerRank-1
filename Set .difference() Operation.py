n = int(input())
e = set(map(int, input().split()))
n = int(input())
f = set(map(int, input().split()))
d=e.difference(f)
print(len(d))
