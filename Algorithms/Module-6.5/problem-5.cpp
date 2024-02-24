#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int height[N];
int visited[N];

void dfs(int node)
{
    visited[node]=1;

    for(auto v : adj[node])
    {
        if(visited[v]) continue;
        dfs(v);
        height[node]= max(height[node],height[v]+1);
        
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
    cout<<"Height of "<< x <<": "<<height[x];
    
     
    return 0;
}