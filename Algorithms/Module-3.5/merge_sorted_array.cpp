class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) 
    {
        int p1=0;
        int p2=0;

        vector<int>v2;

        while(p1< m && p2 < n)
        {
            if(nums1[p1] < nums2[p2])
            {
                v2.push_back(nums1[p1]);
                p1++;
            }
            else
            {
                v2.push_back(nums2[p2]);
                p2++;

            }
        }
        while(p1 < m)
        {
            v2.push_back(nums1[p1]);
            p1++;
        }
        while(p2 < n)
        {
            v2.push_back(nums2[p2]);
            p2++;
        }
        nums1=v2;
        
    }
};