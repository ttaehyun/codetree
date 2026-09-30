arr = list(map(int, input().split()))

n = len(arr)

for i in range(n):
    if arr[i] == 0:
        index = i
        break

sum = 0
for k in range(index-1,index-4,-1):
    # print(k)
    # print(arr[k])
    sum += arr[k]

print(sum)
