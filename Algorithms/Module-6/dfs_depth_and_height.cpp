#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int depth[N];
int height[N];

int visited[N];

void dfs(int node)
{
    cout<<node<<" ";
    visited[node]=1;

    for(auto n : adj[node])
    {
        depth[n]=depth[node]+1;
        dfs(n);
        if(height[n]+1 > height[node])
        {
            height[node]=height[n]+1;
        }
    }

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
        adj[v].push_back(u);
    }
    dfs(1);
     
    return 0;
}