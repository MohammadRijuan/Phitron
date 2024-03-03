//adjacency list diye node konta kontar sthe connected tar list pabo...

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,e;
    cin>>n>>e;
    //adjacency list banate vector lagbe
    vector<int>adj[n+1]; //adj(n+1) dile vector tar size bujabe

    while (e--)
    {
        int a,b;
        cin>>a>>b;
        adj[a].push_back(b);
        adj[b].push_back(a);
        
    }

    for (int i = 0; i <=n; i++)
    {
        cout<<"index of "<<i<<": ";

        for (int j = 0; j <adj[i].size(); j++)
        {
            cout<<adj[i][j]<<" ";
        }
        cout<<endl;
    }
    
     
    return 0;
}