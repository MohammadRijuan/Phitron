#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for (int i = 0; i < n; i++)
    {
        cin>>a[n];
    }
    //int mx=0;
    for (int i = 0; i < n; i++)
    {
        int mx=0;
        if(a[i]>mx)
        {
            a[i]=mx;
            
        }
        mx++;
        cout<<mx<<" ";
    }
    
     
    return 0;
}