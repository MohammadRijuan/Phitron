#include<bits/stdc++.h>
using namespace std;
class student
{
    public :
       char name[100];
       int roll;
       int cls;
       char section;

};
int main()
{
    student s;
    char name[100]="Rijuan";
    s.cls=7;
    s.roll=25;
    s.section='A';

    cout<<s.name<<" ";
    cout<<s.cls<<" ";
    cout<<s.roll<<" ";
    cout<<s.section<<" ";
     
    return 0;
}