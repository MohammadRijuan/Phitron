#include<bits/stdc++.h>
using namespace std;

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
    dsu_set(n);
    while(e--)
    {
        int a,b;
        cin>>a>>b;
        dsu_union(a,b);
    } 
    return 0;
}