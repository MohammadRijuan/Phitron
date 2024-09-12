#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;

const int N=1e3+5;
vector<string>g;
int visited[N][N];
int level[N][N];
//pii parent[N][N];

vector<pii> direc={{0,1},{0,-1},{1,0},{-1,0}};

int n,m;

bool isValid(int i,int j)
{
    return(i>=0 && i< g.size() && j>=0 && j< g[i].size());
}

void bfs(int si,int sj)
{
    queue<pii>q;
    q.push({si,sj});
    visited[si][sj]= 1;
    level[si][sj]=0;
   //parent[si][sj]={-1,-1};
    
    while(!q.empty())
    {
        pii upair=q.front();
        q.pop();

        int i=upair.first;
        int j=upair.second;

        for(auto d : direc)
        {
            int ni= i+ d.first;
            int nj= j+d.second;

            if(isValid(ni,nj) && !visited[ni][nj] && g[ni][nj] !='-')
            {
                q.push({ni,nj});
                visited[ni][nj]=1;
                level[ni][nj]=level[i][j]+1;
                //parent[ni][nj]={i,j};
            }
        }
    }

}

int main()
{
    
    cin>>n>>m;

    int si,sj,di,dj;

    for (int i = 0; i <n; i++)
    {
        string x;
        cin>>x;
        g.push_back(x);
    }

    cin>>si>>sj>>di>>dj;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            level[i][j]=-1;
        }
        
    }
    
    bfs(si,sj);
    

    if(level[di][dj]!=-1) cout<<"YES";
    else cout<<"NO";


    
     
    return 0;
}