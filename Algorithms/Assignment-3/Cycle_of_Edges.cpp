#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
int parent[N];
int parentSize[N];

void dsu_set(int node)
{
    for (int i = 1; i <=node; i++)
    {
        parent[i]=-1;
        parentSize[i]=0;
    }
}

int dsu_find(int node)
{
    while(parent[node]!=-1)
    {
        node=parent[node];
    }
    return node;
}

void dsu_union(int a,int b)
{
    int leaderA=dsu_find(a);
    int leaderB=dsu_find(b);

    if(leaderA!=leaderB)
    {
        if(parentSize[leaderA]> parentSize[leaderB])
        {
            parent[leaderB]=leaderA;
            parentSize[leaderA]+=parentSize[leaderB];
        }
        else if(parentSize[leaderA] < parentSize[leaderB])
        {
            parent[leaderA]=leaderB;
            parentSize[leaderB]+=parentSize[leaderA];

        }
        else
        {
            parent[leaderA]=leaderB;
            parentSize[leaderB]+=parentSize[leaderA];

        }
    }
}
int main()
{
    int n,e;
    cin>>n>>e;

    int cnt=0;

    dsu_set(n);
    while(e--)
    {
        int a,b;
        cin>>a>>b;
        int leaderA=dsu_find(a);
        int leaderB=dsu_find(b);

        if(leaderA == leaderB)
        {
            cnt++; //koita cycle dtect korbe..vector diyeo kora jbe..
        }
        else
        {
            dsu_union(a,b);
        }
    }
    cout<<cnt<<endl;  ///vector diye korle size print korte hbe
    

     
    return 0;
}