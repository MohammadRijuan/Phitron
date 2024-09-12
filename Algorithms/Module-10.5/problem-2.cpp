#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;

const int N=1e5+7;
const int INF=1e9+9;

vector<pii>adj[N];
vector<int>dist(N,INF);

int visited[N];

void dijkstra(int node)
{
    priority_queue<pii,vector<pii>,greater<pii>>pq; 

    dist[node]=0;

    pq.push({dist[node],node});

    while(!pq.empty())
    {
        int p =pq.top().second;
        pq.pop();

        visited[p]=1;

        for(pii vpair : adj[p])
        {
            int v=vpair.first;
            int w=vpair.second;

            if(visited[v]) continue;
            if(dist[v]>dist[p]+w)
            {
                dist[v]=dist[p]+w;
                pq.push({dist[v],v});
            }
        }
    }


}

int main()
{
    int n,m;
    cin>>n>>m;
    for (int i = 0; i <m; i++)
    {
        int u,v,w;
        cin>>u>>v>>w;
        adj[u].push_back({v,w});
    }

    int s,d;
    cin>>s>>d;
    dijkstra(s);

    cout<<dist[d]<<endl;
    
     
    return 0;
}