#include<bits/stdc++.h>
using namespace std;

const int N = 1e5 + 5;
vector<int> adj[N];
bool visited[N];

// নোডে ডিপথ ফালানোর জন্য একটি ডিপথ প্রবাহ ফাংশন
void dfs(int node, vector<int> &component) 
{
    // নোডটি ভিজিট করা হয়েছে
    visited[node] = true;
    // কম্পোনেন্টে নোডটি সংযুক্ত করুন
    component.push_back(node);

    // সকল সংযুক্ত নোডগুলির জন্য রিকার্সিভ dfs কল
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
    // নোড এবং এজের সংখ্যা পড়ুন
    int n, m;
    cin >> n >> m;

    // এজ তালিকা তৈরি করুন
    for (int i = 0; i < m; i++) 
    {
        int u, v;
        cin >> u >> v;
        // গ্রাফে u থেকে v এবং v থেকে u এজ সংযোজন করুন
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    // সংযুক্ত কম্পোনেন্ট সংরক্ষণ করার জন্য ভেক্টর
    vector<vector<int>> components;

    // সকল নোড পরীক্ষা করুন
    for (int i = 1; i <= n; i++) 
    {
        // ভিজিটেড না হলে
        if (visited[i]==0) 
        {
            // একটি নতুন কম্পোনেন্টের জন্য ভেক্টর তৈরি করুন
            vector<int> component;
            // dfs কল করুন এবং কম্পোনেন্টে সংযুক্ত নোডগুলি সংরক্ষণ করুন
            dfs(i, component);
            // কম্পোনেন্ট সংরক্ষণ করুন
            components.push_back(component);
        }
    }

    // সংযুক্ত কম্পোনেন্টগুলি প্রিন্ট করুন
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
