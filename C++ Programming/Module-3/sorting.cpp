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
    //sorting
    //sort(a,a+n); //choto teke boro ei niyome
    sort(a,a+n,greater<>()); //boro teke choto ei niyome
    for (int i = 0; i < n; i++)
    {
        cout<<a[i]<<" ";
    }
    
    return 0;
}