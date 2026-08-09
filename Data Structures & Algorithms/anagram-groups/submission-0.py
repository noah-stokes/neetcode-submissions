class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        
        for i in range(0,len(strs)):
            sorted_s = sorted(strs[i])
            dict[tuple(sorted_s)] = []
        
        for i in range(0,len(strs)):
            sorted_s = sorted(strs[i])
            dict[tuple(sorted_s)].append(strs[i]) 
        return dict.values()

        
            
            

