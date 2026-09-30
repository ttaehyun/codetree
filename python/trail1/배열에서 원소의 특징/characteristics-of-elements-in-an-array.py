arr = list(map(int, input().split()))

index = 0
for i in range(len(arr)):
    if arr[i] % 3 == 0:
        # index = i
        print(arr[i-1])
        break
    