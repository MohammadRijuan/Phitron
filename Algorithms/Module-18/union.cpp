#include<bits/stdc++.h>
using namespace std;

int parent[1000];

void dsu_set(int node)
{
    for (int i = 1; i <=node; i++)
    {
        parent[i]=-1;
    }
}

int dsu_find(int node)   //leader kuje r banai
{
    while(parent[node]!=-1)
    {
        node=parent[node];
    }
    return node;
}

void dsu_union(int a,int b)  //2ta group er leader teke 1ta leader k fixed kore
{
    int leaderA=dsu_find(a);
    int leaderB=dsu_find(b);

    if(leaderA!=leaderB)
    {
        parent[leaderB]=leaderA;
    }
}
int main()
{
    int n,e;
    cin>>n>>e;
    while(e--)
    {
        int a,b;
        cin>>a>>b;
        dsu_union(a,b);
    }
     
    return 0;
}