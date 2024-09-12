/*input

5
7
1 2 2
1 3 6
2 3 1
3 4 4
4 2 6
2 5 3
5 4 9

*/
#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;
const int N=1e3+7;
const int INF=1e9+10;
int d[N][N];
int n,m;

void dist_initialize()
{
    for (int i = 1; i <=n; i++)
    {
        for (int j = 1; j <=n; j++)
        {
            if(i!=j)
            {
                d[i][j]=INF;
            }
        }
        
    }
    
}

void print_matrix()
{
    for (int i = 1; i <=n; i++)
    {
        for (int j = 1; j <=n; j++)
        {
            if(d[i][j]==INF) cout<<"X"<<" ";
            else cout<<d[i][j]<<" ";
        }
        cout<<endl;
        
    }
    
}
int main()
{
    cin>>n>>m;

    dist_initialize();
    
    while(m--)
    {
        int u,v,w;
        cin>>u>>v>>w;
        d[u][v]=w;
    }

    print_matrix();

    for (int k = 1; k <=n; k++) //level akare korbe...int k level...
    {
        for (int i = 1; i <=n; i++)
        {
            for (int j = 1; j <=n; j++)
            {
                d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
            }
            
        }
        
    }
    cout<<"after floyd warshall "<<endl;
    print_matrix();
    

    
     
    return 0;
}