#include<bits/stdc++.h>
using namespace std;
int main()
{
    //list<int>mylist(10,5);
    //list<int>mylist;
    //cout<<mylist.size();

    //cout<<mylist.front();

    /*for (auto it =mylist.begin(); it != mylist.end(); it++) //loop diye size deka jabena atai...iterator diye dekte hobe
    {
        cout<<*it<<endl<<endl;
    }*/

    /*list<int>int2={1,2,3,4,5};
    list<int>mylist(list2);
    for (auto it =mylist.begin(); it != mylist.end(); it++)
    {
        cout<<*it<<endl;
    }*/
    
    /*int a[5]={10,20,30,40,50};
    list<int>mylist(a,a+5);
    for (auto it =mylist.begin(); it != mylist.end(); it++)
    {
        cout<<*it<<endl;
    }*/

    vector<int>v={100,200,300};
    list<int>mylist(v.begin(),v.end());
    /*for (auto it =mylist.begin(); it != mylist.end(); it++)
    {
        cout<<*it<<endl;
    }*/

    for(int val : mylist)  // amar value lagtese index lagtese na...tai eibaveo kora jabe..
    {
        cout<<val<<endl;
    }




     
    return 0;
}