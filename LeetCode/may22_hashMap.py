t = int(input())
for _ in range(t):
    def two_sum(arr, target):
        table = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in table:
                return [table[complement], i]
            table[num] = i
        return []  

    arr = list(map(int, input().split()))
    target = int(input())
    result = two_sum(arr, target)
    print(result)

