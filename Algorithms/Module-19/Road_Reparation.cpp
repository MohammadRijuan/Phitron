#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;
const int N=1e5+5;
vector<pii>v[N];
int visited[N];

class Edge
{
    public:
    int a,b,w;

    Edge(int a,int b,int w)
    {
        this->a=a;
        this->b=b;
        this->w=w;
    }
};

class cmp
{
    public:
    bool operator()(Edge a , Edge b)
    {
        return a.w > b.w;
    }
};

void prims_algo(int s,int n)
{
    priority_queue<Edge,vector<Edge>,cmp> pq;

    pq.push(Edge(s,s,0));

    vector<Edge> edgelist;
    int cnt=0;

    while(!pq.empty())
    {
        Edge parent = pq.top();
        pq.pop();

        int a=parent.a;
        int b=parent.b;
        int w=parent.w;

        if(visited[b]) continue;
        visited[b]=true;

        cnt++;

        edgelist.push_back(parent);

        for (int i = 0; i < v[b].size(); i++)
        {
            pii child=v[b][i];

            if(!visited[child.first])
            {
                pq.push(Edge(b,child.first,child.second));
            }
        }
    }
    edgelist.erase(edgelist.begin());

    long long int sum=0;

    for(Edge v : edgelist)
    {
        sum+=(long long)(v.w);
    }

    if(cnt==n)
    {
        cout<<sum<<endl;
    }
    else
    {
        cout<<"IMPOSSIBLE"<<endl;
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
        v[a].push_back({b,w});
        v[b].push_back({a,w});
    } 
    prims_algo(1,n);
    return 0;
}

