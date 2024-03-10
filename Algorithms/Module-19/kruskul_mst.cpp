#include<bits/stdc++.h>
using namespace std;

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


bool cmp(Edge a , Edge b)
{
    return a.w > b.w;
}

int parent[1000];
int parentlevel[1000];

void dsu_set(int node)  //parent ke -1 kore dibo detect korte easy hbe
{
    for (int i = 1; i <=node; i++)
    {
        parent[i]=-1;
        parentlevel[i]=0;
    }
}

int dsu_find(int node)  //leader banabe
{
    while(parent[node]!=-1)  
    {
        node=parent[node]; //j node e -1 kuje pabe oitai parent
    }
    return node;
}

void dsu_union(int a,int b)  //2ta grp er maje connection korte jekono ekta grp er leader er sthe connect kore 1ta companion banano
{
    int leaderA=dsu_find(a);
    int leaderB=dsu_find(b);

    if(leaderA!=leaderB)
    {
        //A ke leader banalam
        if(parentlevel[leaderA] > parentlevel[leaderB]) //Aer level boro hole
        {
            parent[leaderB]=leaderA;
        }
        else if(parentlevel[leaderA] < parentlevel[leaderB])
        {
            //B ke leader banalam
            parent[leaderA]=leaderB;
        }
        else
        {
            //jekono ekjn leader hbe
            parent[leaderB]=leaderA;
            parentlevel[leaderA]++;  //je hbe oi group leader er level barbe jehetu onno grp jukto hbe tai
        }
    }
}
int main()
{
    int n,e;
    cin>>n>>e;

    vector<Edge>ans;
    vector<Edge>v;
    dsu_set(n);

    while(e--)
    {
        int a,b,w;
        cin>>a>>b>>w;

        v.push_back(Edge(a,b,w));
    }
    sort(v.begin(),v.end(),cmp);
    for(Edge val : v)
    {
        int a=val.a;
        int b=val.b;
        int w=val.w;

        int leaderA=dsu_find(a);
        int leaderB=dsu_find(b);

        if(leaderA==leaderB)
        {
            continue;
        }
        ans.push_back(val);
        dsu_union(a,b);
    }

    for(Edge val : ans)
    {
        cout<<val.a<<" "<<val.b<<" "<<val.w<<endl;
    }


     
    return 0;
}