#include<bits/stdc++.h>
using namespace std;
int main()
{
    list<int>mylist={10,20,30,40,50};
    //cout<<mylist.front();
    //cout<<mylist.back();
    cout<< *next(mylist.begin(),3)<<endl; //internal pblm er karone iterator k access korte deyna..tai ata k dereferrence korte hbe nahole man  40 pabona
    return 0;
}