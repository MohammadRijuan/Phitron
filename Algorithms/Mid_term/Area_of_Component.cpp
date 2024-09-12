#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;
const int N=1e3+5;
vector<string>g;

int visited[N][N];
int level[N][N];

vector<pii>direc={{0,1},{0,-1},{1,0},{-1,0}};

int xyz=0;

bool isValid(int i,int j)
{
    return (i>=0 && i< g.size() && j>=0 && j< g[i].size());
}

void  bfs(int si , int sj)
{
    queue<pii>q;
    q.push({si,sj});
    visited[si][sj]=1;
    level[si][sj]=0;

    while(!q.empty())
    {
        xyz++;
        pii upair = q.front();
        q.pop();

        int i= upair.first;
        int j= upair.second;

        for(auto d : direc)
        {
            int ni= i +d.first;
            int nj= j+d.second;

            if(isValid(ni,nj) && !visited[ni][nj] && g[ni][nj] != '-')
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
    int n, m;
    cin >> n >> m;

    //int si, sj, di, dj;

    for(int i = 0; i < n; i++)
    {
        string x;
        cin >> x;

        g.push_back(x);
    }

    
    int minn = INT_MAX;
    
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            level[i][j]=-1;
        }
    }
    
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < m; j++)
        {
            if(visited[i][j] == 0 && g[i][j] == '.')
            {
                xyz = 0;
                bfs(i, j);
                minn = min(xyz, minn);
            }
        }
    }

    minn = min(xyz, minn);
    if(minn == 0) cout <<"-1";
    else cout << minn;
}