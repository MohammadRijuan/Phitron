#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector <int> v={1,2,2,3,4,5,1,2,4,5,3,2};
    replace(v.begin(),v.end()-1,2,100); //v.end e v.end(-1) dewai seser 2 replace korte pareni
    
    for(int x: v)
    {
        cout<<x<<" ";
    } 
    return 0;
}