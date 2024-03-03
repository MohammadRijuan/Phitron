//edge list ber koprbo eibve

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,e;
    cin>>n>>e;

    vector<pair<int,int>>v;  //vector pair nite hbe..
    while(e--)
    {
        int a,b;
        cin>>a>>b;
        v.push_back({a,b});
    } 

    for (int i = 0; i <v.size(); i++)
    {
        cout<<v[i].first<<" "<<v[i].second<<endl; //v[i] dile onek error asbee...
    }
    
    return 0;
}