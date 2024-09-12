#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>mylist={10,20,30};
    //cout<<mylist.max_size(); 
    //mylist.clear(); .//ata dile list clear hoye jabe

    //mylist.resize(2);
    //mylist.resize(5);
    mylist.resize(5,2);
    cout<<mylist.size()<<endl;
    for(int val : mylist)  // amar value lagtese index lagtese na...tai eibaveo kora jabe..
    {
        cout<<val<<endl;
    }
    return 0;
}