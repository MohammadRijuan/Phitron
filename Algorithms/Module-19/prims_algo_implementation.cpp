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

    bool operator()(Edge a,Edge b)
    {
        return a.w > b.w; //it will sort the weight of b
    }
};

void prims_algo(int s)
{
    priority_queue <Edge,vector<Edge>,cmp> pq;
    pq.push(Edge(s,s,0));

    vector<Edge>Edge_list;

    while(!pq.empty())
    {
        Edge parent =pq.top();
        pq.pop();

        int a=parent.a;
        int b=parent.b;
        int w=parent.w;

        if(visited[b]) continue;
        visited[b]=1;

        Edge_list.push_back(parent);

        for (int i = 0; i <v[b].size(); i++)
        {
            pii child= v[b][i];

            if(!visited[child.first])
            {
                pq.push(Edge(b,child.first,child.second));
            }
        }
    }
    Edge_list.erase(Edge_list.begin());

    for (Edge val : Edge_list)
    {
        cout<<val.a<<" "<<val.b<<" "<<val.w<<endl;
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
    prims_algo(1);
     
    return 0;
}