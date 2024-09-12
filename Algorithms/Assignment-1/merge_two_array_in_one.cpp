#include<bits/stdc++.h>
using namespace std;

void merge_sort (int arr1[] ,int m,int arr2[], int n,int ans[])
{
    int p1=0;
    int p2=0;

    int s=0;

    while(p1 < m && p2 < n)
    {
        if(arr1[p1] > arr2[p2])
        {
            ans[s++]=arr1[p1++];
        }
        else
        {
            ans[s++]=arr2[p2++];
        }        
    }

    while( p1 < m)
    {
        ans[s++]=arr1[p1++];
    }
    while( p2 < n)
    {
        ans[s++]=arr2[p2++];
    }
    
    
}


int main()
{
    
    int m;
    cin>>m;
    int arr1[m];

    for (int i = 0; i < m; i++)
    {
        cin>>arr1[i];
    }
    
    int n;
    cin>>n;
    int arr2[n];

    for (int i = 0; i < n; i++)
    {
        cin>>arr2[i];
    }
    int ans[m+n];

    merge_sort(arr1,m,arr2,n,ans);

    for (int i = 0; i < m+n; i++)
    {
        cout<<ans[i]<<" ";
        
    }
    return 0;
}