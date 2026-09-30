arr = list(map(int, input().split()))
n = len(arr)
sum_val = 0
for i in range(1, n, 2):
    sum_val+= arr[i]
# print(sum_val)
filter1 = arr[2::3]

print(sum_val, sum(filter1) / len(filter1))
# print(filter1)