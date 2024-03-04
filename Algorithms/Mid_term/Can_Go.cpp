#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;

const int N=1e3+5;
const int INF=1e9+5;

vector<pii>adj[N];
int visited[N];
int level[N];
vector<int>dist(N,INF);

void dijkstra(int src)
{
    priority_queue<pii,vector<pii>,greater<pii>>pq;
    dist[src]=0;
    pq.push({dist[src],src});
    visited[src]=1;
    level[src]=0;

    while(!pq.empty())
    {
        int p=pq.top().second;
        pq.pop();

        visited[p]=1;

        for(pii vpair : adj[p])
        {
            int v= vpair.first;
            int w= vpair.second;

            if(visited[v]) continue;
            if(dist[v] > dist[p]+w)
            {
                dist[v]=dist[p]+w;
                pq.push({dist[v],v});
            }
        }
    }


}

int main()
{
    int n,e;
    cin>>n>>e;
    while(e--)
    {
        int a,b,w;
        cin>>a>>b>>w;
        adj[a].push_back({b,w});
    } 

    int s,t;
    cin>>s>>t;
    dijkstra(s);

    while(t--)
    {
        int d,dw;
        cin>>d>>dw;
        if(dist[d] <= dw)
        {
            cout<<"YES"<<endl;
        }
        else
        {
            cout<<"NO"<<endl;
        }
    }
    return 0;
}