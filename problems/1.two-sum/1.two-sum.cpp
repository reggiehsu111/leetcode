class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
    	unordered_map<int, int> m;
        vector<int> ret(2, 0);
        for (int i=0; i<nums.size(); i++) {
            if (m.find(nums[i]) != m.end()) {
                ret[0] = m[nums[i]];
                ret[1] = i;
                return ret;
            } else {
                m[target - nums[i]] = i;
            }
        }
        return ret;    
    }
};
