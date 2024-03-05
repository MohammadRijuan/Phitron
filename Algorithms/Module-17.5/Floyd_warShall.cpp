#include<bits/stdc++.h>
using namespace std;

const int INF=1e7;

int main()
{
    int n;
    cin>>n;
    int dist[n+1][n+1];

    for (int i = 0; i <=n; i++)
    {
        for (int j = 0; j <=n; j++)
        {
            if(i!=j)
            dist[i][j]=INF;

        }
        
    }

    for (int i = 0; i <n; i++)
    {
        for (int j = 0; j <n; j++)
        {
            cin>>dist[i][j];

        }
        
    }

    //floyd_warshall
    for (int k=0; k <n; k++)
    {
        for (int i = 0; i <n; i++)
        {
           for (int j = 0; j <n; j++)
           {
               
               dist[i][j]=min(dist[i][j],dist[i][k] + dist[k][j]);

           }
        
        }

    }

    for (int i = 0; i <n; i++)
        {
           for (int j = 0; j <n; j++)
           {
               
               if(dist[i][j]==INF) cout<<"X"<<" ";
               else
               cout<<dist[i][j]<<" ";

           }
           cout<<endl;
        
        }
    



     
    return 0;
}