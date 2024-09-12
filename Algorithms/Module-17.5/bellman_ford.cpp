#include<bits/stdc++.h>
using namespace std;

const int INF=1e7;
class  Edge
{
    public:
    int u;
    int v;
    int w;

    Edge(int u,int v,int w)
    {
        this->u=u;
        this->v=v;
        this->w=w;
    }
};
int main()
{
    int n,e;
    cin>>n>>e;

    vector<Edge>v;

    while(e--)
    {
        int a,b,w;
        cin>>a>>b>>w;

        Edge ed(a,b,w);
        v.push_back(ed);
    } 

    int dist[n+1];

    for (int i = 1; i <=n; i++)
    {
        dist[i]=INF;
    }
    dist[1]=0;

    for (int i = 1; i <=n-1; i++)
    {
        for (int j = 0; j <v.size(); j++)
        {
            Edge ed=v[j];

            int a=ed.u;
            int b=ed.v;
            int w=ed.w;

            if(dist[a] < INF && dist[b] > dist[a]+w) //dist[a] < INF neg value er jonno
            {
                dist[b]=dist[a]+w;
            }
        }
        
    }
    for (int i = 1; i <=n; i++)
    {
        if(dist[i]==INF) cout<<"30000"<<endl; //neg value er jonno
        else
        cout<<dist[i]<<" "<<endl;; 
    }
    
    
    
    return 0;
}