#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];
int level[N];

void bfs(int node)
{
    for(int i=0;i<N;i++)
    {
        visited[i]=0;
        level[i]=-1;
    }
    queue<int>q;
    q.push(node);
    visited[node]=1;
    level[node]=0;

    while(!q.empty())
    {
        int p=q.front();
        q.pop();

        for(auto v : adj[p])
        {
            if(visited[v]==0)
            {
                q.push(v);
                level[v]=level[p]+1;
                visited[v]=1;
            }
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

    int Q;
    cin>>Q;

    while(Q--)
    {
        int s,d;
        cin>>s>>d;

        bfs(s);

        cout<<level[d]<<endl;


    }
     
    return 0;
}