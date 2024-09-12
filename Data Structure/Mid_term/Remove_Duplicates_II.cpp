#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>mylist;
    int val;
    while(true)
    {
        cin>>val;
        if(val==-1) break;
        mylist.push_back(val); //value add korbe
    } 
    mylist.sort(); //sort korbe...sort korle unique kaj korbe, onnothay korbena..
    mylist.unique(); //unique nymber guloy print korbe

    for(int val : mylist)
    {
        cout<<val<<" ";

    }
    return 0;
}