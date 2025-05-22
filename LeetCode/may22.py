t = int(input())
for _ in range(t):
    def two_sum(nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # nums = [1, 5, 2, 11, 15, 7]
    arr = list(map(int, input().split()))
    target = int(input())
    result = two_sum(arr, target)
    print(result)
