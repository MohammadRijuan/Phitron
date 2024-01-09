#include<iostream>
#include<iomanip> //setprecision er jonno ei header
using namespace std;
int main()
{
    float a;
    cin>>a;
    cout<<fixed<<setprecision(2)<<a; //2 ghor nile c++ e setprecision diye (desire ghor) dite hbe
    return 0;
}