#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
vector<int>adj[N];
int visited[N];

void bfs(int node)
{
    queue<int>q;
    stack<int>st;

    visited[node]=1;
    q.push(node);

    while(!q.empty())
    {
        int p=q.front();
        q.pop();
        st.push(p);

        for ( auto v : adj[p])
        {
            if(visited[v]) continue;
            q.push(v);
            visited[v]=1;
        }
    }
    while(!st.empty())
    {
        cout<<st.top()<<" ";
        st.pop();
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
    bfs(1);
    
     
    return 0;
}