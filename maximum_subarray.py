def maxSubArray(nums):

    #we are taking two varible total_sum and max_sum
    #total_sum will take care of sum till every index and max_sum will the max(total_sum, max_sum)
    total_sum = max_sum = nums[0]
     #in starting we are giving value to both total_sum and max_sum as value at index 0   
    for i in nums[1:]: #looping the array starting from index 1

        total_sum = max(i, total_sum + i) #computing total sum
        max_sum = max(total_sum, max_sum) # updating max_sum if total_sum is larger than max_sum
        
    return max_sum