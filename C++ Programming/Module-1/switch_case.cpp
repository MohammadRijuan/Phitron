#include<iostream>
using namespace std;
int main()
{
    int v;
    cin>>v;
    switch(v)
    {
        case 1:
        cout<<"one"<<" ";
        break;

        case 2:
        cout<<"two"<<" ";
        break;

        case 3:
        cout<<"three"<<"";
        break;

        case 4:
        cout<<"four"<<" ";   //jodi break na di four o print korbe
        break;

        case 5:
        cout<<"five"<<" ";
        break;

        default :
        cout<<"didnt match"<<endl;
    }
    return 0;
}