#include<bits/stdc++.h>
using namespace std;


void merge(int a[],int l, int m, int r)
{
    int leftSize=(m-l+1);
    int rightSize=(r-m);

    int L[leftSize];
    int R[rightSize];

    int k=0;

    for (int i = l; i <=m; i++) //l=0 theke suru korbe m porjnto
    {
        L[k]=a[i];
        k++;
    }
    k=0;
    for (int i = m+1; i <=r; i++)//m+1 teke suru korbe...r porjnto colbe
    {
        R[k]=a[i];
        k++;
    }
    int i=0,j=0;
    int curr=l;

    while(i < leftSize && j < rightSize)
    {
        if(L[i] <= R[j])
        {
            a[curr]=L[i];  //a[] current e update korlam left side ta..
            i++;
        }
        else
        {
            a[curr]=R[j]; //a[] current e update korlam rightt side ta..
            j++;
        }
        curr++;
    }
    

    while(i < leftSize)
    {
        a[curr]=L[i];
        i++;
        curr++;
    }
    while(j < rightSize)
    {
        a[curr]=R[j];
        j++;
        curr++;
    }
}
void merge_sort(int a[],int l,int r)
{
    if(l<r)
    {
        int mid=(l+r)/2;
        merge_sort(a,l,mid);
        merge_sort(a,mid+1,r);

        merge(a,l,mid,r);
        
    }
}
int main()
{
    int n;
    cin>>n;
    int a[n];

    for (int i = 0; i <n; i++)
    {
        cin>>a[i];
    }

    merge_sort(a,0,n-1);
    
    for (int i = 0; i <n ; i++)
    {
        
        cout<<a[i]<<" ";
    }

    
    
    
     
    return 0;
}