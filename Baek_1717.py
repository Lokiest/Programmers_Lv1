import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
        return parent[x]
    return x


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


n, m = map(int, input().split())
parent = [0] * (n + 1)
for i in range(n + 1):
    parent[i] = i

for i in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        if find(b) == find(c):
            print('yes')
        else:
            print('no')
    else:
        union(b, c)
