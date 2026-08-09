class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for i in range(0,len(nums)):
            print(str(nums[i]))
            if str(nums[i]) in hash.keys():
                return 'true'
            else:
                hash[str(nums[i])] = []
        return 'false'
        
       


        
        