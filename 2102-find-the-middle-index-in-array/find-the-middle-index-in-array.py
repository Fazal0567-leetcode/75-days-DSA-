class Solution(object):
    def findMiddleIndex(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        leftSum = 0 
        rightSum = sum(nums)

        for i in range (len(nums)):
            if leftSum == rightSum - nums[i]:
                return i 

            leftSum += nums[i]
            rightSum -= nums[i]

        return -1