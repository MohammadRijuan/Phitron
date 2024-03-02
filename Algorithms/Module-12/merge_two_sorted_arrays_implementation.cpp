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
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    } 

    merge(a,0,3,n-1);

    for (int i = 0; i <n; i++)
    {
        cout<<a[i]<<" ";
    }
    
    return 0;
}