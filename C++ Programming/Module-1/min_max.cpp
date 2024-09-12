#include<iostream>
#include<algorithm>
using namespace std;
//int my_min(int a,int b)
//{
    //if(a>b) return b;
    //else return a;
//}
//int my_max(int a,int b)
//{
    //if (a<b) return b;
    //else return a;
//}
int main()
{
    int a, b;
    cin>>a>>b;
    int mn=min(a,b); //min max diley easily vber kore dibe ata holo builtin function
    int mx=max(a,b);
    cout<<mx<<" " <<mn;
    return 0;
}