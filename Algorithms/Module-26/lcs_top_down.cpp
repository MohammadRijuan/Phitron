#include<bits/stdc++.h>
using namespace std;

int dp[1005][1005];

int lcs(string a,int n,string b,int m)
{
    //base case
    if (n==0 || m==0)
    {
        return 0;
    } 
    if (dp[n][m]!=-1) return dp[n][m];
    //last element mil hole
    if(a[n-1] == b[m-1])
    {
        int ans=lcs(a,n-1,b,m-1); //er agher gulo niye kaj korbe

        return ans+1;
    }
    //mil na hole last element
    else
    {
        int ans1=lcs(a,n-1,b,m); //a- er last element agher ta r b- er last elemnt niye kaj korbe
        int ans2=lcs(a,n,b,m-1); // same vabe b- er last element agher ta r a- er last elemnt niye kaj korbe

        return max (ans1,ans2);
    }
}
int main()
{
    string a,b;
    cin>>a>>b;

    //memset (dp,-1,sizeof (dp)); //same as dp[i][j]=-1

    for (int i = 0; i <=a.size (); i++)
    {
        for (int j = 0; j <=b.size (); j++)
        {
            dp[i][j]=-1;
        }
        
    }
    
    cout<<lcs (a,a.size (),b, b.size ());

    return 0;
}