#include<bits/stdc++.h>
using namespace std;

vector<int> sort (vector<int>&v ,int l, int r)
{
    if( l < 0 || r >= v.size()) return {};
    if(l==r) return {v[l]};

    int mid=(l+r)/2;
    vector<int> left = sort(v,l,mid);
    vector<int> right = sort(v,mid+1,r);

    int p1=0;
    int p2=0;

    vector <int>v2;

    while(p1 < left.size() && p2 < right.size())
    {
        if(left[p1] > right[p2])
        {
            v2.push_back(left[p1]);
            p1++;
        }
        else
        {
            v2.push_back(right[p2]);
            p2++;
        }
    }

    while( p1 < left.size())
    {
        v2.push_back(left[p1]);
        p1++;
    }
    while( p2 < right.size())
    {
        v2.push_back(right[p2]);
        p2++;
    }

    return v2;
}

void merge_sort(vector<int>&v)
{
    v=sort(v,0,v.size()-1);
}
int main()
{
    vector<int> v;
    //cin>>v;
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