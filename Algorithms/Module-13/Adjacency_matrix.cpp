//adj matrix diye kon kon tar edge ase dekte parbo but osngoko sonkar ber kora possible na...tar jonno adj list lagbe

#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,e;
    cin>>n>>e;
    int adj[n+1][n+1]; //ata array diye kora jbe

    for (int i = 0; i <=n; i++)
    {
        for (int j = 0; j <=n; j++)
        {
            adj[i][j]=0;   //if(i==j) adj[i][j]=1 dile corner borabor sob  1hye jbe

        }
        
    }
    

    for (int i = 0; i <n; i++)
    {
        int a,b;
        cin>>a>>b;
        adj[a][b]=1; //a,b 1 korbe edge onusare
        adj[b][a]=1;
    }

    for (int i = 0; i <=n; i++)
    {
        for (int j = 0; j <=n; j++)
        {
            cout<<adj[i][j]<<" ";  //print korbe matrix ta
        }
        cout<<endl;
        
    }
     
    return 0;
}