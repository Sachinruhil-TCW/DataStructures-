


'''
count = 0
n= len(nums)
prefix = 0 for in range(n+1)
for i in range(1,n+1):
    prefix[i] = prefix[i-1]+nums[i-1]
    #{for this above line of code if nums = [1,2,3,4,5], prefix will be [0,1,3,6,10,15]}
for start in range(n):
    for end in range(start + 1, n+1):
        if prefix[end]-prefix[start]==k:
            count = count +1
return count



count = 0
n= len(nums)

for start in range(n):
    cumulative_sum= 0
    for end in range(start + 1, n+1):
        cumulative_sum += nums[end]
        if cu=mulative_sum ==k:
            count = count +1
return count

 
'''#in other words we need to find the range start and end 
#where cumulativesum[end]- cumulativesum[start] = k
# or you can say sum[start] = sum[end]- k

sumdict = {0:1}
n = len(nums)
count = 0
s = 0

for nums i ums:
    s += num
    if s-k in sumdict:
        count += sumdict[s-k]
    sumdict[s] = sumdict.get(s,0)+1
return count



