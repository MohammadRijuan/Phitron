#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    cin.ignore(); //space soho nicce tai cin.ignore() dite hobe
    vector<string>v(n);
    for (int i = 0; i < n; i++)
    {
        getline(cin,v[i]);
    }
    for (string val : v)
    {
        cout<<val<<endl;
    }
    
     
    return 0;
}