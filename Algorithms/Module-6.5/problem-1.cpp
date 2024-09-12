#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];

void dfs(int node)
{
    visited[node]=1;

    for(auto v : adj[node])
    {
        if(visited[v]) continue;
        dfs(v);
    }
    cout<<node<<" ";
}

int main()
{
    int n,m;
    cin>>n>>m;
    for (int i = 0; i < m; i++)
    {
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
    }

    dfs(1);
    return 0;
}