#include<bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;
const int N=1e3+5;

vector<string>g;

int visited[N][N];
int level[N][N];

vector<pii>direc={{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

bool isValid(int i, int j)
{
    return (i >= 0 && i < g.size() && j >= 0 && j < g[i].size());
}

void bfs(int si,int sj)
{
    queue<pii>q;
    q.push({si,sj});
    visited[si][sj];
    level[si][sj]=0;

    while(!q.empty())
    {
        pii upair = q.front();
        q.pop();

        int i=upair.first;
        int j=upair.second;

        for(auto d : direc)
        {
            int ni= i+d.first;
            int nj= j+d.second;

            if(!visited[ni][nj] && isValid(ni,nj) && g[ni][nj]!='x')
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
    int n,m;
    cin>>n>>m;

    int si,sj,di,dj;

    for (int i = 0; i < n; i++)
    {
        string x;
        cin>>x;
        for (int j = 0; j < m; j++)
        {
            if(x[j]=='s')
            {
                si=i;
                sj=j;
            }
            if(x[j]=='e')
            {
                di=i;
                dj=j;
            }
        }
        g.push_back(x);
        
    }

    bfs(si,sj);

    if(level[di][dj]!=0)
    {
        cout<<level[di][dj]<<endl;
    }
    else
    {
        cout<<"-1"<<endl;
    }
     
    return 0;
}