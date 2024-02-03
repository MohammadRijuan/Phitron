#include<bits/stdc++.h>
using namespace std;
int main()
{
    set<int>s; // set alwz sorted akare man dey, duplicate remove kore dey..reverse function diye reverse kora jaina but vector e niye reverse kora jabe....
    int n;
    cin>>n;

    while(n--)
    {
        int x;
        cin>>x;
        s.insert(x);
    } 
    for (auto it = s.begin(); it!=s.end(); it++)
    {
        cout<<*it<<endl;
    }

    cout<<s.count(1000)<<endl; //jeta inpurt dbona oita 0 dibe
    
    return 0;
}