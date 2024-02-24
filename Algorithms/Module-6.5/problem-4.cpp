#include<bits/stdc++.h>
using namespace std;

const int N=1e3+5;
vector<int>adj[N];
int depth[N];
int visited[N];

void dfs(int node)
{
    visited[node]=1;

    for(auto v : adj[node])
    {
        if(visited[v]) continue;
        depth[v]=depth[node]+1;
        dfs(v);
    }
}

int main()
{
    int n,m;
    cin>>n>>m;

    for (int i = 0; i <m ; i++)
    {
        int u,v;
        cin>>u>>v;
        adj[v].push_back(u);
        adj[u].push_back(v);
    }
    dfs(1);

    int x;
    cin>>x;
    cout<<"Depth of "<< x <<": "<<depth[x];
    
     
    return 0;
}