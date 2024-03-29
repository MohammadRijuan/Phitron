#include<bits/stdc++.h>
using namespace std;

int max(int n,int s, int v[],int w[])
{
    int dp[n+1][s+1];
    dp[0][0]=1;

    for (int i = 1; i <=s ; i++)
    {
        dp[0][i]=0;
    }

    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= s; j++)
        {
            if(i==0 || j==0)
            {
                dp[i][j]=0;
            }

            else if(w[i-1] <= j)
            {
                dp[i][j]=max(dp[i-1][j-w[i-1]] + v[i-1] , dp[i-1][j]);
            }

            else
            {
                dp[i][j]=dp[i-1][j];
            }
        }
        
    }
    return dp[n][s];
    
    
}
int main()
{
    int t;
    cin>>t;

    while (t--)
    {
        int n,s;
        cin>>n>>s;

        int v[n],w[n];

        for (int i = 0; i < n; i++)
        {
            cin>>w[i];
        }

        for (int i = 0; i < n; i++)
        {
            cin>>v[i];
        }

        cout<<max(n,s,v,w)<<endl;;


    }
     
    return 0;
}