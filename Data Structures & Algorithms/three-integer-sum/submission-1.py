class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -1 * nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                if nums[l] + nums[r] == target:
                    if (nums[i],nums[l],nums[r]) not in res:
                        res.add((nums[i],nums[l],nums[r]))
                    l += 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        final = []

        for val in res:
            final.append(list(val))
        
        return final
