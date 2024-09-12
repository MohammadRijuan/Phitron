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
            level[v]=level[p]+1;
            parent[v]=p;
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

    int s,d;
    cin>>s>>d;
    
    bfs(s);

    cout<<"Distance :"<<level[d]<<endl;

    vector<int>path;

    int current=d;

    while(current != -1)
    {
        path.push_back(current);
        current=parent[current];
    }
    reverse(path.begin(),path.end());

    cout<<"path :";

    for(auto node : path)
    {
        cout<<node<<" ";
    }





    
     
    return 0;
}