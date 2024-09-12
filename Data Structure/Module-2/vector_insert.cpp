#include<bits/stdc++.h>
using namespace std;
int main()
{
    /* vector <int>  v = {1,2,3,4,5};
    for(int x : v) //shortcut loop index chara..chaileo index pabo na
    {
        cout<<x<<" ";
    } */

    /* vector <int> v = {1,2,3,4,5};
    v.insert(v.begin()+2 , 10); //2no index e 10 value input kore asbe 1 2 10 3 4 5
    for(int x : v)
    {
        cout<<x<<" ";
    } */

    vector <int> v = {1,2,3,4,5};
    vector <int> v2 = {100,101,102,103};
    v.insert(v.begin()+2 , v2.begin() , v2.end()); //arekta vector insert korle output amon asbe 1 2 100 101 102 103 3 4 5 
    for(int x : v)
    {
        cout<<x<<" ";
    }
    return 0;
}