#include<bits/stdc++.h>
using namespace std;

int min_conquer(vector<int>&v,int l, int r)
{
    if(l< 0 || r>=v.size()) return INT_MAX;
    if(l==r) return {v[l]};

    int mid=(l+r)/2;

    int left=min_conquer(v,l,mid);
    int right=min_conquer(v,mid+1,r);

     return min(left,right);

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
    cout<<min_conquer(v,0,v.size()-1);
     
    return 0;
}



/* void min_conquer(vector<int>& v, int l, int r, int& result)
{
    if(l < 0 || r >= v.size())
    {
        result = INT_MAX;
        return;
    }
    if(l == r)
    {
        result = v[l];
        return;
    }

    int mid = (l + r) / 2;

    int left, right;

    min_conquer(v, l, mid, left);
    min_conquer(v, mid + 1, r, right);

    result = min(left, right);
}*/