#include<bits/stdc++.h>
using namespace std;
int main()
{
    string a="Hello";
    string b="World";
    //string c=a+b; //a.append(b)-> likha mane holo a+b;
    //cout<<a<<endl; 
    //cout<<b<<endl; 
    //cout<<c<<endl;

    //a="HelloA";// works
    //a=a+b;  //works
    a[5]='A'; //didnt work
    //a.push_back('A'); //works
    //eigulor jekono ekta kora jabe expand er khetre
    //a.pop_back(); //ata diye last character remove kore jotobar dibo tar last er ta cole jbe
    //cout<<a<<endl;

    //a="Gelo";
    //a.assign("Gelo");
    //cout<<a<<endl;

    a="Hello_World";
    //a.erase(4,1); //a.erase(index,word or length)
    //a.replace(4,0,"so");
    //a.insert(5,"Rijuan");
    cout<<a<<endl;

    return 0;
}