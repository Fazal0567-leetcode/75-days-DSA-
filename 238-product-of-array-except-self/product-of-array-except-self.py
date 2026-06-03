class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [1] * n

        #prefix product 
        pre = 1 
        for i in range(n):
            ans[i] = pre
            pre *= nums[i]


        #suffix product 
        suff = 1 
        for i in range(n - 1 , -1 , -1):
            ans[i] *= suff
            suff *= nums[i]

        return ans