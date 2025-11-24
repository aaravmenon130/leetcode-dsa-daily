#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        d = {}
        for i, val in enumerate(s):
            if val not in d:
                d[val] = i
        return [d[i] for i in nums]
