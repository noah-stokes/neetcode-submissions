class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0 : 1}
        s = 0
        res = 0
        for i in range(len(nums)):
            s += nums[i]
            pfs = s - k

            # check if we have needed prefix
            if pfs in prefixSum:
                res += prefixSum[pfs]

            # add new prefix sum
            if s not in prefixSum:
                prefixSum[s] = 1
            else: 
                prefixSum[s] += 1
            
        return res
            
            