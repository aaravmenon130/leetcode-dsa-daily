#https://leetcode.com/problems/set-mismatch/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        d1 = defaultdict(int)

        missing_value = 0
        repeated_value = 0

        for i in range(n):
            if nums[i] in d1:
                repeated_value = nums[i]

            if i + 1 not in nums:
                missing_value = i + 1

            d1[nums[i]] += 1
                
        return [repeated_value, missing_value]
