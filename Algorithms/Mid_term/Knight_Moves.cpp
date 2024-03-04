#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;

const int N=1e3+5;

int visited[N][N];
int level[N][N];

vector<pii>direc={{2,1},{2,-1},{-2,1},{-2,-1},{1,2},{1,-2},{-1,2},{-1,-2}};
//int n,m;

bool isValid(int i,int j,int n,int m)
{
    return(i>=0 && i< n && j>=0 && j< m);
}

void bfs(int si,int sj,int n,int m)
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            visited[i][j]=0;
            level[i][j]=-1;
        }    
    }

    queue<pii>q;

    q.push({si,sj});
    visited[si][sj]=1;
    level[si][sj]=0;

    while(!q.empty())
    {   
        pii upair= q.front();
        q.pop();

        int i=upair.first;
        int j=upair.second;

        for(auto d : direc)
        {
            int ni= i +d.first;
            int nj= j +d.second;

            if(isValid(ni,nj,n,m) && !visited[ni][nj])
            {
                q.push({ni,nj});
                visited[ni][nj]=1;
                level[ni][nj]=level[i][j]+1;

            }
        }
    }

}


int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        int n,m;
        cin>>n>>m;

        int ki,kj,Qi,Qj;
        cin>>ki>>kj>>Qi>>Qj;

        bfs(ki,kj,n,m);

        cout<<level[Qi][Qj]<<endl;


    }
     
    return 0;
}