#include<bits/stdc++.h>
using namespace std;
void print(stringstream & ss) //stringstream alwz & dite hbe
{
    string word;
    if(ss>>word)
    {
        //cout<<word<<endl; //serially asbe
        print(ss);
        cout<<word<<endl; //reverse akare asbe
    }

}
int main()
{
    string s;
    getline(cin,s);
    stringstream ss(s);
    print(ss);

    return 0;
}