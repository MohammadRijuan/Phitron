/*input
5 8
########
#..##..#
####.#.#
#..#...#
########

output
3
*/


#include <bits/stdc++.h>
using namespace std;

typedef pair<int,int>pii;
const int N = 1e3 + 5;
vector<string> g;
bool visited[N][N];
int n,m;
vector<pii>direction={{0,1},{0,-1},{1,0},{-1,0}};

int isValid(int i, int j)
{
    return (i >= 0 && i <n && j >= 0 && j < m); //validity check...
}

void dfs(int i, int j)
{
    if (!isValid(i, j)) return; //asole valid kina node e dukte parbe kina..
    if(visited[i][j]) return; //aghe visit korse kina...
    if(g[i][j] == '#') return; //wall ase kina


    visited[i][j] = true;
    //upore ,niche,side e check korbe...

    for(auto d : direction)
    {
        dfs(i+d.first,j+d.second);

        /*dfs(i, j + 1); 
        dfs(i, j - 1);
        dfs(i + 1, j);
        dfs(i - 1, j);*/

    }
}

int main()
{
    
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        string x;
        cin >> x;
        g.push_back(x);
    }

    int cnt = 0;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (g[i][j] == '#') continue; 
            if(visited[i][j])
                continue;

            dfs(i, j);
            cnt++;
        }
    }

    cout << cnt << endl;

    return 0;
}
