//koita component r max size ber kora tader

#include<bits/stdc++.h>
using namespace std;

int parent[1000];
int parentSize[1000];

int mx=0;

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
            mx=max(mx,parentSize[leaderA]); 
        }
        else
        {
            parent[leaderA]=leaderB; 
            parentSize[leaderB]+=parentSize[leaderA];
            mx=max(mx,parentSize[leaderB]); 
        }
    }
}


int main()
{
    int n,e;
    cin>>n>>e;
    dsu_set(n);
    int component=n; //n nilam karon joto ase to to ta

    while(e--)
    {
        int a,b;
        cin>>a>>b;

        int leaderA=dsu_find(a);
        int leaderB=dsu_find(b);

        if(leaderA!=leaderB)  //aladha aladha leader hole
        {
            component--;
            dsu_union(a,b);
        }
        cout<<component<<" "<<mx<<endl;  /// বাকি থাকা সংগঠনের সংখ্যা এবং সবচেয়ে বড় সাইজটি প্রিন্ট করলাম
        
    }



    return 0;
}