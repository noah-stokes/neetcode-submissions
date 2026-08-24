#include <unordered_map>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int l = nums.size();

        std::unordered_map<int, int> dict;

        for(int i = 0; i < l; i++) {
            if (dict.count(nums[i])) {
                return true;
            }
            dict[nums[i]] = 0;
        }

        return false;
    }
};