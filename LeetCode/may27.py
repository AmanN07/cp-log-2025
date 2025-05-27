def median(num1, num2):
    if len(num1) > len(num2):
        num1, num2 = num2, num1

    x, y = len(num1), len(num2)
    low, high = 0, x
    
    while low <= high:
        partitionX = (low+high)//2
        partitionY = (x + y + 1) //2 - partitionX

        maxLeftX = float('-inf') if partitionX == 0 else num1[partitionX - 1]
        minRightX = float('inf') if partitionX == x else num1[partitionX]

        maxLeftY = float('-inf') if partitionY == 0 else num2[partitionY - 1]
        minRightY = float('inf') if partitionY == y else num2[partitionY]

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if (x + y) % 2 == 0:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY)) / 2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1


num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
print(median(num1, num2))
