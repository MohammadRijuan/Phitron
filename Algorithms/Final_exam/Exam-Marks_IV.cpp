#include<bits/stdc++.h>
using namespace std;

const int mod =1e9+7;
int dp[1005][1005];

int maxFunc (int n,int m,int a[])
{
    if (m==0) return 1;
    if (n==0) return 0;

    if (dp[n][m] != -1)
    {
        return dp[n][m];
    }

    if (a[n-1]<=m)
    {
        int marks1 =maxFunc (n-1,m-a[n-1],a);
        int marks2 =maxFunc (n-1,m,a);

        return dp[n][m]= (marks1 + marks2) % mod;
    }
    
}

int main()
{
    int t;
    cin>>t;

    while (t--)
    {
        int n,m;
        cin>>n>>m;

        int a[n];

        for (int i = 0; i <n; i++)
        {
            cin>>a[i];
        }

        int sum=1000-m;

        for (int i = 0; i <=n; i++)
        {
            for (int j = 0; j <=sum; j++)
            {
                dp[i][j]=-1;
            }
        }

        cout<<maxFunc (n,m,a)<<endl;

    } ! & %
     
    return 0;
}