def search(self, nums: List[int], target: int) -> int:

        
        
        if not nums:
            return -1

        low, high = 0, len(nums) - 1 # took low and high

        while low <= high:
            mid = (low + high) // 2 # we will calculate mid every time
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:  #that means first half is sorted
                if nums[low] <= target <= nums[mid]: #it means the target lies in first half
                    high = mid - 1
                else:
                    low = mid + 1 #other wise we will search is second half
            else:   
			#here it means that the first half is not in ascending order
                if nums[mid] <= target <= nums[high]: #if it lies in second half
                    low = mid + 1 
                else:
                    high = mid - 1 #if not we will search in first half

        return -1