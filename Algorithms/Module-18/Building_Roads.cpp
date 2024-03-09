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
        parentSize[i]=1;
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
        if(parentSize[leaderA] > parentSize[leaderB])
        {
            parent[leaderB]=leaderA;
            parentSize[leaderA]+=parentSize[leaderB];
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

    map<int,bool>mp;  // ম্যাপ তৈরি করলাম

for (int i = 1; i <=n; i++)
{
    int leader=dsu_find(i); // নোড i এর লিডার বের করলাম
    mp[leader]=true; // লিডারটি ম্যাপে চিহ্নিত করলাম
}
vector<int>v;  
for (pair<int,bool> p : mp)
{
    v.push_back(p.first);  // ভেক্টরে লিডারগুলি যোগ করলাম
}

cout<<v.size()-1<<endl;  // ভেক্টরের সাইজ প্রিন্ট করলাম

for (int i = 0; i <v.size()-1; i++)
{
    cout<<v[i]<< " "<<v[i+1]<<endl;  // এই লিডারগুলির মধ্যে সংযোগ তৈরি করে প্রিন্ট করলাম
}

    
    
    return 0;
}