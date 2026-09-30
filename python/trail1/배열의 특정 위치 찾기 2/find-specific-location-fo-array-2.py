arr = list(map(int,input().split()))

sum_eval = 0
sum_odd = 0
# print(arr)
for i in range(0,len(arr),2):
    sum_eval += arr[i]
    sum_odd += arr[i+1]

if sum_eval > sum_odd:
    print(sum_eval - sum_odd)
elif sum_eval < sum_odd:
    print(sum_odd - sum_eval)
else:
    print(0)