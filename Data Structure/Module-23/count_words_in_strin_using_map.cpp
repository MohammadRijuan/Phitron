#include<bits/stdc++.h>
using namespace std;
int main()
{
    string sentence;
    getline(cin,sentence);

    string words;
    stringstream ss(sentence);
    /* while(ss >> words)
    {
        cout<<words<<endl;
    }*/

    map<string,int>mp;
    while(ss >> words)
    {
        mp[words]++;
    }
    /* for (auto it = mp.begin(); it!=mp.end(); it++)
    {
        cout<<it->first<<" "<<it->second<<endl;
    } */

    cout<<mp["cricket"]<<endl;
    
     
    return 0;
}