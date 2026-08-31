class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroes = 0
        product = 1
        for num in nums:
            if num == 0:
                zeroes += 1
            else:
                product *= num
        
        sol = []

        for i in range(len(nums)):
            if zeroes >= 2:
                ES = 0
            elif zeroes == 1:
                if nums[i] == 0:
                    ES = product
                else:
                    ES = 0
            else:
                ES = product // nums[i]
            sol.append(ES)
        return sol
            

