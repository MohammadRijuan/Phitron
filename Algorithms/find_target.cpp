class Solution {
public:
    vector<int> targetIndices(vector<int>& nums, int target) 
    {
        sort(nums.begin(),nums.end()); //sort korlam

        vector<int>v; //ekta vector nilam

        int n=nums.size();
        
        for(int i=0;i<n; i++)
        {
            if(nums[i] == target)
            {
                v.push_back(i); //vector e push korlam...jeta mile jabe oitai print korbe..
            }
        }
        return v; //oitai ferot dilam...
    }
};