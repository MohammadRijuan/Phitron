#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];

int dfs(int node)
{
    visited[node]=1;
    int cnt=0;
    for(auto v : adj[node])
    {
        if(visited[v]) continue;
        visited[v]=1;
        cnt=cnt + dfs(v);
        cnt++;
    }
    return cnt;
}

int main()
{
    int n,m;
    cin>>n>>m;

    for (int i = 0; i < m; i++)
    {
        int u,v;
        cin>>u>>v;
        //for directly
        adj[u].push_back(v);
        //adj[v].push_back(u);
    }
    int x;
    cin>>x;

    int v=dfs(x);
    cout<<v<<" ";


    
     
    return 0;
}