#include<bits/stdc++.h>
using namespace std;

int unbounded_knapsack(int v[],int w[], int n, int s)
{
    if(n==0 || s==0) return 0;

    if(w[n-1] <= s)
    {
    int choice1=v[n-1] + unbounded_knapsack(v,w,n,s- w[n-1]);
    int choice2=unbounded_knapsack(v,w,n-1,s);

    return max(choice1,choice2);
    }
    else
    {
        return unbounded_knapsack(v,w,n-1,s);

    }
}
int main()
{
    int n,s;
    cin>>n>>s;
    int v[n],w[n];

    for (int i = 0; i < n; i++)
    {
        cin>>v[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin>>w[i];
    }

    cout<<unbounded_knapsack(v,w,n,s);
     
    return 0;
}