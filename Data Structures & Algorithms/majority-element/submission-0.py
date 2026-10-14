class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        m = nums[0]
        for num in nums:
            freq[num] += 1
            if freq[num] > freq[m]:
                m = num
        
        return m