#include<bits/stdc++.h>
using namespace std;

vector<int> sort(vector<int>&v ,int l, int r)
{
    if(l < 0 || r>= v.size()) 
    {
        return {};
    }
    if(l==r)
    {
        return {v[l]};
    }

    int mid=(l+r)/2;

    vector<int>left=sort(v,l,mid);
    vector<int>right=sort(v,mid+1,r);

    int p1=0;
    int p2=0;

    vector<int>v2;

    while(p1 < left.size() && p2 < right.size())
    {
        if(left[p1] < right[p2])
        {
            v2.push_back(left[p1]);
            p1++;

        }
        else
        {
            v2.push_back(right[p2]);
            p2++;
        }

    }// uporer purota dile only left er single value print dibe

    while(left[p1] < right[p2]) 
    {
        v2.push_back(left[p1]);
        p1++;

    }
    while(left[p1] > right[p2]) 
    {
        v2.push_back(right[p2]);
        p2++;

    }
    // uporer 2ta nile left,right sb dibe...
    return v2;
}

void merge_sort(vector<int>&v)
{
    
    v=sort(v,0,v.size()-1);

}
int main()
{
    vector<int>v;; //={12,7,3,9,18,2,5,4};
    int n;
    cin>>n;
    for (int i = 0; i < n; i++)
    {
        int x;
        cin>>x;
        v.push_back(x);
    }
    merge_sort(v);

    for (int i = 0; i < n; i++)
    {
        cout<<v[i]<<" ";
    }
    


    


    return 0;
}