from itertools import permutations

def f(B, x):
    for perm in permutations(B):
        res = x
        for b in perm:
            res %= b
        if res == y:
            return True

T = int(input())
for _ in range(T):
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    result = []
    for k in range(1, n+1):
        if f(A[:k], x):
            result.append(k)
    print(len(result))
    print(" ".join(map(str, result)))

