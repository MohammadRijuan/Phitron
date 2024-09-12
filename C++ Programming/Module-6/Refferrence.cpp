#include<bits/stdc++.h>
using namespace std;
void change(string& s) //& eikane referrence hisebe kaj kore...& dile world print hbe...na dile main er hello e print hobe
{
    s="world";
}
int main()
{
    string s="hello";
    change(s);
    cout<<s<<endl;

    return 0;
}