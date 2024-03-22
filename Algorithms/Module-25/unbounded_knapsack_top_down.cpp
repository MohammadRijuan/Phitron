#include<bits/stdc++.h>
using namespace std;

int dp[1005][1005];

int unbounded_knapsack(int v[],int w[], int n, int s)
{
    if(n==0 || s==0) return 0;

    if(dp[n][s]!=-1) return dp[n][s];

    if(w[n-1] <= s)
    {
    int choice1=v[n-1] + unbounded_knapsack(v,w,n,s- w[n-1]);
    int choice2=unbounded_knapsack(v,w,n-1,s);

    return dp[n][s]=max(choice1,choice2);
    }
    else
    {
        return dp[n][s]=unbounded_knapsack(v,w,n-1,s);

    }
}
int main()
{
    int n,s;
    cin>>n>>s;
    int v[n],w[n];

    for (int i = 0; i <=n; i++)
    {
        for (int j = 0; j <=s; j++)
        {
            dp[i][j]=-1;
        }
        
    }
    

    for (int i = 0; i < n; i++)
    {
        cin>>v[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin>>w[i];
    }

    cout<<unbounded_knapsack(v,w,n,s);
     
    return 0;
}