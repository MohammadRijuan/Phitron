#include<bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
vector<int> adj[N];
bool visited[N];

void dfs(int node, vector<int> &component) 
{
    visited[node] = true;
    component.push_back(node);

    for (auto v : adj[node]) 
    {
        if (visited[v]==0) 
        {
            dfs(v, component);
        }
    }
}

int main() 
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) 
    {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    vector<vector<int>> components;
    for (int i = 1; i <= n; i++) 
    {
        if (visited[i]==0) 
        {
            vector<int> component;
            dfs(i, component);
            components.push_back(component);
        }
    }

    for (int i = 0; i < components.size(); i++) 
    {
        cout << "Component " << i + 1 << " :";
        for (int j = 0; j < components[i].size(); j++) 
        {
            cout << " " << components[i][j];
        }
        cout << endl;
    }


    return 0;
}
