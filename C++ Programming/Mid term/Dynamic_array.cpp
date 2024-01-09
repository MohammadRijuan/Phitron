#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int *array = new int[n]; // allocate korlam (new) niye int k
    for (int i = 0; i < n; i++)
    {
        array[i]=i+1;   //tarpor value assign korlam.. 
    }
    for (int i = 0; i < n; i++)
    {
        cout<<array[i]<<" "; //output ber korlam array tar
    }
    delete []array; //array ta deallocate kore dilam 
    
    return 0;
}