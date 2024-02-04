#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    cin.ignore(); // ata na dile newline nicce na

    while(t--)
    {
        string s;
        getline(cin,s);

        string word;
        stringstream ss(s);

        map<string,int>mp;

        while(ss >> word)
        {
            mp[word]++;
        }
        int max=INT_MIN;
        for (auto it = mp.begin(); it!= mp.end(); it++)
        {
            if(it->second > max)
            {
                max=it->second;
            } 
            //cout<<word<<" "<<max<<endl; //ata output progress 4 dicce....  
        }

        stringstream sent(s);
        map<string,int>m;
        string words;
        
        while(sent >> words)
        {

            m[words]++;

            if(m[words]==max)
            {
                cout<<words<<" "<<max<<endl;
                break;
            }
        }
        
        
    } 
    return 0;
}