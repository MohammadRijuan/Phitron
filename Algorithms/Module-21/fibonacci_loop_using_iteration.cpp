#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n;
    cin>>n;
    long long a[n+1];
    a[0]=1; 
    a[1]=1;

    for (long long i = 2; i <=n; i++)
    {
        a[i]=a[i-1] + a[i-2];
    }
    cout<<a[n];
     
    return 0;
}