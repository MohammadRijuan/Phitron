#include<bits/stdc++.h>
using namespace std;

int max_conquer(vector<int>&v,int l, int r)
{
    if(l< 0 || r>=v.size()) return INT_MIN;
    if(l==r) return {v[l]};

    int mid=(l+r)/2;

    int left=max_conquer(v,l,mid);
    int right=max_conquer(v,mid+1,r);

    return max(left,right);

}
int main()
{
    vector<int>v;
    int n;
    cin>>n;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin>>x;

        v.push_back(x);
    }
    cout<<max_conquer(v,0,v.size()-1);
     
    return 0;
}