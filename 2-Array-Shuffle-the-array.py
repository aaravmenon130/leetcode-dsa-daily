#https://leetcode.com/problems/shuffle-the-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i = 0
        ans = []
        while i < n:
            ans.append(nums[i])
            ans.append(nums[i + n])
            i += 1
        return ans
