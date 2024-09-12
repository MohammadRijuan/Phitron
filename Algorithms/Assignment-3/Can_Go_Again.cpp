#include<bits/stdc++.h>
using namespace std;
const int INF=1e9+5;

class Edge
{
    public:
    int a,b;
    long long w;

    Edge(int a,int b,long long w)
    {
        this->a=a;
        this->b=b;
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
        int a,b;
        long long w;
        cin>>a>>b>>w;
        
        Edge ed(a,b,w);
        v.push_back(ed);
    }

    int s=0;
    cin>>s;
    vector <long long> dis(n+1,INF); //int e nile exact ans pawa jbe na...jehetu w er exact ekta constrains dewa ache...so long long e korte hbe 
    for (int i = 1; i <=n; i++)
    {
        dis[i]=INF;
    }
    
    dis[s]=0;

    for (int i = 1; i <=n-1; i++)
    {
        for (int j = 0; j < v.size(); j++)
        {
            Edge ed=v[j];

            int a=ed.a;
            int b=ed.b;
            long long w=ed.w;

            if(dis[a]!=INF && dis[a] + w < dis[b])
            {
                dis[b]=dis[a]+w;
            }

        }
        
    }
    bool cycle=false;

    for (int j=0; j< v.size() ;j++)
    {
        Edge ed=v[j];

        int a=ed.a;
        int b=ed.b;
        long long w=ed.w;

        if(dis[a]!=INF && dis[a] + w < dis[b])
        {
            cycle=true;
            break;
            dis[b]=dis[a]+w;
        }

    }
    int t;
    cin>>t;
    while (t--)
    { 
        int d;
        cin >> d;

        if (cycle)
        {
            cout << "Negative Cycle Detected" << endl;
            return 0;
        }
        else if (dis[d] == INF)
        {
            cout << "Not Possible" << endl;
        }
        else
        {
            cout << dis[d] << endl;
        }
    }  
     
    return 0;
}