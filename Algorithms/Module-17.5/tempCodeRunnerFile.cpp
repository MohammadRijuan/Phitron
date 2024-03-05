#include<bits/stdc++.h>
using namespace std;

const int INF=1e7;

int main()
{
    int n;
    cin>>n;
    int dist[n+1][n+1];

    for (int i = 0; i <n; i++)
    {
        for (int j = 0; j <n; j++)
        {
            if(i!=j)
            dist[i][j]=INF;
        }
        
    }

    for (int i = 0; i <=n; i++)
    {
        for (int j = 0; j <=n; j++)
        {

            int a;
            cin>>a;
            if(a!=-1) dist[i][j]=-1;
        }
        
    }

    //after flyd warshall
    int maxx=INT_MIN;

    for (int k = 0; k <n; k++)
    {
        for (int i = 0; i <n; i++)
    {
        for (int j = 0; j <n; j++)
        {
            dist[i][j]=min(dist[i][j],dist[i][k] + dist[k][j]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if(dist[i][j]==INF) continue;
            maxx=max(dist[i][j],maxx);

        }       
    }
    cout<<maxx<<endl;
    
}   
    
     
    return 0;
}