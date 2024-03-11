#include<bits/stdc++.h>
using namespace std;

const long N=1e3+5;
const long INF=1e15+5;

long long dis[N][N];
long long n,e;

void dist_initialize()
{
    for (long long i = 1; i <=n; i++)
    {
        for (long long j = 1; j <=n; j++)
        {
            if(i != j)
            {
                dis[i][j]=INF;
            }
        }
    }
}

/*void print_matrix()
{
    for (long long i = 1; i <=n; i++)
    {
        for (long long j = 1; j <=n; j++)
        {
            if(dis[i][j]==INF) cout<<"X"<<endl;
            else
            cout<<dis[i][j]<<" ";
        }
        cout<<endl;
    }
    //cout<<endl;
}*/

int main()
{
    //int n,e;
    cin>>n>>e;

    dist_initialize();

    while(e--)
    {
        long long a,b,w;
        cin>>a>>b>>w;
        dis[a][b]=min(dis[a][b],w);
    }

    //print_matrix();

    for (long long k = 1; k <=n; k++)
    {
        for (long long i = 1; i <=n; i++)
        {
            for (long long j = 1; j <=n; j++)
            {
                dis[i][j]=min(dis[i][j],dis[i][k] + dis[k][j]);
            }
        }
    }

    long long q;
    cin>>q;

    while(q--)
    {
        long long a,b;
        cin>>a>>b;

        if(dis[a][b]==INF) cout<<"-1"<<endl;
        else cout<<dis[a][b]<<endl;
    }
    
    return 0;
}