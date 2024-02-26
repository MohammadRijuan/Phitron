#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;
const int N=1e5+5;
const int INF=1e9+10;

vector<pii>adj[N];
int visited[N];
vector<int>dist(N,INF);
int parent[N];

void dijkstra(int src)
{
    priority_queue<pii,vector<pii>,greater<pii>>pq;
    dist[src]=0;
    pq.push({dist[src],src});

    while(!pq.empty())
    {
        int p= pq.top().second;
        pq.pop();

        visited[p]=1;

        for(pii vpair : adj[p])
        {
            int v =vpair.first;
            int w =vpair.second;

            if(visited[v] > dist[p]+w)
            {
                dist[v]=dist[p]+w;
                pq.push({dist[v],v});
                parent[v]=p;
            }
        }

    }
}

void print_shortest(int src,int des)
{
    dijkstra(src);
    stack<int>st;

    int current=des;

    while(current!= -1)
    {
        st.push(current);
        current=parent[current];
    }
    cout << "distance of shortest path: " << dist[des] << endl;

    cout << "shortest path: ";

    while(!st.empty())
    {
        cout << st.top() << " ";
        st.pop();
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
        adj[v].push_back({u,w});
    }

    print_shortest(1,7);
    

    return 0;
}