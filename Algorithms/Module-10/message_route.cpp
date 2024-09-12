#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];
int level[N];
int parent[N];

void bfs(int node)
{
    queue<int>q;
    q.push(node);
    visited[node]=1;
    level[node]=0;
    parent[node]=-1;

    while(!q.empty())
    {
        int p=q.front();
        q.pop();

        for(auto v : adj[p])
        {
            if(visited[v]) continue;
            q.push(v);
            visited[v]=1;
            parent[v]=p;
            level[v]=level[p]+1;
        }
    }
}
int main()
{
    int n,m;
    cin>>n>>m;

    for(int i=0;i<m;i++)
    {
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    } 

    bfs(1);

    vector<int>path;

    cout<<level[n]<<endl;

    int curr=n;

    while(curr != -1)
    {
        path.push_back(curr);
        curr=parent[curr];
    }
    reverse(path.begin(),path.end());
    for(auto l : path)
    {
        cout<< l <<" ";
    }


    return 0;
}