#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cin>>s;
    //sort(starting pointer, ending pointer)
    //sort(s.begin(),s.end()); //ogochalo serially korbe..
    sort(s.end(),s.begin()); //eibve segmentaion fault dibe
    cout<<s<<endl;
    return 0;
}