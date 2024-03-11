#include<bits/stdc++.h>
using namespace std;

const int N=1e5+5;
long long save[N];

long long fibo(long long n)
{
    if(n==0 || n==1)
    return 1;

    if(save[n]!=-1)
    {
        return save[n];
    }
    long long ans1=fibo(n-1);  
    long long ans2=fibo(n-2);

    save[n]=ans1+ans2;

    return save[n];  
}
int main()
{
    long long n;
    cin>>n;

    for (long long i = 0; i <=n; i++)
    {
        save[i]=-1;
    }
    
    cout<<fibo(n)<<endl;

    return 0;
}

//2^n complexity komanor jnno amra ekta array nibo jetate agher memory gulo save kore rakbo jar fole agher gulo r call hbena...r er maddome n  songkok e call korbe..then complexity O(n) hbe
//100 input dile read korte onk tym lagbe tai llong long diye korbo sob ,er maddome 100 er jonno 19digit er ekta man asbe..
