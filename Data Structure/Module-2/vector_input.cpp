#include<bits/stdc++.h>
using namespace std;
int main()
{
    //vector <int> v;
    //int n;
    //cin >> n;

    //wrong type

    /* for (int i = 0; i < n; i++)
    {
        cout<<v[i]<<" ";  //direct v[i] newa jai na
    } */

    //1st type

    /* for (int i = 0; i < n; i++)
    {
        int x;
        cin>>x;
        v.push_back(x);
    }
    for(int val : v)
    {
        cout<<val<<" ";
    } */

    //2nd type
    
    int n;
    cin>>n;
    vector<int>v(n);
    for (int i = 0; i < n; i++)
    {
        cin>>v[i];
    }
    for (int val : v)
    {
        cout<<val<<" ";
    }
    
    return 0;
}