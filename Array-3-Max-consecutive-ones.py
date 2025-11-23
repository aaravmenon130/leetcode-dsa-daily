#https://leetcode.com/problems/max-consecutive-ones/submissions/1837392367/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxx = 0
        arr = []
        for i in nums:
            if i == 1:
                maxx += 1
            else:
                maxx = 0
            arr.append(maxx)
        return max(arr)
