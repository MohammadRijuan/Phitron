#include<iostream>
using namespace std;
int main()
{
    char a;
    cin>>a;
    switch(a)
    {
        case 'a':
        cout<<"vowel"<<endl;
        break;

        case 'e':
        cout<<"vowel"<<endl;
        break;

        case 'i':
        cout<<"vowel"<<endl;
        break;

        case 'o':
        cout<<"vowel"<<endl;   //jodi break na di four o print korbe
        break;

        case 'u':
        cout<<"vowel"<<endl;
        break;

        default :
        cout<<"consonant"<<endl;
    }
    return 0;
}