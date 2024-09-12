#include<bits/stdc++.h>
using namespace std;
int main()
{
    //string s="hello world";
    //cout<<s.size()<<endl; 
    //cout<<s.max_size()<<endl; // 10^6 porjnto nite pare

    //string a= "trfjhfhsrthr";
    //cout<<a.capacity()<<endl;
    //a="hfkhfgkjhgcvkjhdlfghsdlghlsdjh";
    //cout<<a.capacity()<<endl;

    //string s="hello";
    //cout<<s<<endl;
    //s.clear();
    //cout<<s<<endl;
    //cout<<s.size()<<endl;

    //string s="hello";
    //s.clear();
    //if(s.empty()==true) cout<<"empty"<<endl;
    //else cout<<"not empty"<<endl;

    string s;
    cin>>s;
    s.resize(5);
    //s.resize(8); -> eibane dite hbe 
    //s.resize(20,'x');
    //cout<<s.size()<<endl;
    //cout<<s<<endl;
    s.resize(5);
    cout<<s<<endl;
    s.resize(11,'x');
    cout<<s<<endl;
    return 0;
}