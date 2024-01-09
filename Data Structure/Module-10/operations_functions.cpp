#include<bits/stdc++.h>
using namespace std;
int main()
{
    /*list<int>mylist={10,20,30,40,10,10};
    mylist.remove(10);
    for(int val : mylist)
    {
        cout<<val<<endl;
    } */

    list<int>mylist={10,20,30,40,10,10};
    mylist.sort(); //serial korbe
    mylist.sort(greater<int>());  //boro theke choto korbe
    mylist.unique();
    mylist.reverse();
    for(int val : mylist)
    {
        cout<<val<<endl;
    }
    return 0;
}