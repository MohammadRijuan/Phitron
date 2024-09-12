#include<bits/stdc++.h>
using namespace std;

int parent[1000];
int parentSize[1000];

void dsu_set(int node)  //parent ke -1 kore dibo detect korte easy hbe
{
    for (int i = 1; i <=node; i++)
    {
        parent[i]=-1;
        parentSize[i]=1; //parent size ke 1 korlam
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

void dsu_union(int a,int b)
{
    int leaderA=dsu_find(a);
    int leaderB=dsu_find(b);
    
    if(leaderA!=leaderB)
    {
        if(parentSize[leaderA] > parentSize[leaderB]) //size jeta boro oita grp er e leader hbe onno grp er leader
        {
            parent[leaderB]=leaderA;  //A leader
            parentSize[leaderA]+=parentSize[leaderB]; //connect korar por size baralam A leader grp err 
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
    dsu_set(n);

    while(e--)
    {
        int a,b;
        cin>>a>>b;
        dsu_union(a,b);
    } 
    return 0;
}