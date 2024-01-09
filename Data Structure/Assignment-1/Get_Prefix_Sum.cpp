#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    
    }
    long long pre[n];
    pre[0]=a[0]; // index 0 er man nij tekey korte hbe
    for (int i = 1; i < n; i++)
    {
        pre[i]=a[i]+pre[i-1];
    }
    reverse(pre,pre+n);
    for (int i =0; i <=n-1; i++)
    {
        cout<<pre[i]<<" ";
    }
    return 0;
}