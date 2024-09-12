#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];
int level[N];

bool found=false;

void bfs(int node,int l)
{
    for (int i = 0; i <N; i++)
    {
        level[i]=-1;
        visited[i]=0;
    }
    
    queue<int>q;
    
    q.push(node);

    visited[node]=1;
    level[node]=0;

    if(level[node]==l)
    {
        found =true;
    }

    while(!q.empty())
    {
        int p=q.front();
        q.pop();

        for(auto v : adj[p])
        {
            if(visited[v]==0)
            {
                if(level[p]+1==l)
                {
                   found=true;
                }

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
    int l;
    cin>>l;
    bfs(0,l);
    if(found)
    {
        for (int i = 0; i <N; i++)
        {
          if(level[i]==l) 
          {
            cout<< i<<" ";
          }
        }
    }
    else
    {
        cout<<-1;
    }
    
    
     
    return 0;
}