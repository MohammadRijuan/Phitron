#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];

void dfs(int node,int &cnt)
{
    visited[node]=1;
    cnt++;
    for(auto v : adj[node])
    {
        if(visited[v]) continue;
        dfs(v,cnt);
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

    vector<int>ans;

    for (int i = 0; i <N; i++)
    {
        if(visited[i]) continue;
        
        int count=0;
        dfs(i,count);

        if(count> 1)
        {
            ans.push_back(count);
        }
    }
    sort(ans.begin(),ans.end());

    for(int cc : ans)
    {
        cout<<cc<<" ";
    }
    
    
     
    return 0;
}