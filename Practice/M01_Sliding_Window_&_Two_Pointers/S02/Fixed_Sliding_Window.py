"Leetcode 643Q) Maximum Average Subarray"
"Traditional Approach"
from typing import List
def findMaxAverage( nums: List[int], k: int) -> float:
        max_sum = float("-inf")
        n = len(nums)
        for i in range(0,n-k+1):
            sub_sum = 0
            for j in range(i,k+i):
                sub_sum += nums[j]
            max_sum = max(max_sum,sub_sum)
        return max_sum/k
nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums,k))

"Sliding window method"
def findMaxAverage_Optimal(nums: List[int], k: int) -> float:
    max_sum = sum(nums[0:k])
    n = len(nums)
    for i in range(n-k):
        next_sum = max_sum - nums[i] + nums[k+i]
        max_sum = max(next_sum,max_sum)
    return max_sum/k 
nums = [1,12,-5,-6,50,3]
k = 4 
print(findMaxAverage_Optimal(nums,k))

"Leetcode 1343Q) Number of Subarray"

def numOfSubarrays( nums: List[int], k: int, threshold: int) -> int:
        win_sum = sum(nums[0:k])
        count = 0
        if (win_sum/k) >= threshold:
            count+=1
        n = len(nums)
        for i in range(n-k):
            win_sum = win_sum - nums[i]+nums[k+i]
            if (win_sum/k) >= threshold:
                count += 1
        return count
nums = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5
print(numOfSubarrays(nums,k,threshold))

"Leetcode 1456Q) Maximum number of vowels"
