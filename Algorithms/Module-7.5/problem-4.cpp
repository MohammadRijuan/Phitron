#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
bool visited[N];

void dfs(int node)
{
    visited[node]=true;

    for(auto v : adj[node])
    {
        if(visited[v]) continue;
        dfs(v);
    }
}

int main()
{
    int n,m;
    cin>>n>>m;

    for (int i = 0; i <m; i++)
    {
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    int cc=0;
    for (int i = 1; i <= n; i++)
    {
        if(visited[i]) continue;
        dfs(i);
        cc++;
    }
    cout<<"number of connected components :"<< cc <<endl;
    
    
     
    return 0;
}