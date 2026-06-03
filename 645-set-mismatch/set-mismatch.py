class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        duplicate = sum(nums) - sum(set(nums))
        missing = n * (n + 1) // 2 - (sum(nums) - duplicate)

        return [duplicate , missing]