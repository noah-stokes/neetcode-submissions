class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> dict;

        for (int i = 0; i < nums.size(); ++i) {
            int compliment = target - nums[i];

            if (dict.count(compliment)) {
                return {dict[compliment], i};
            }

            dict[nums[i]] = i;
        }

        return {};
    }
};
