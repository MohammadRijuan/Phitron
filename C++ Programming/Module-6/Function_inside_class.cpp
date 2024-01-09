#include<bits/stdc++.h>
using namespace std;
class person
{
    public : 
       string name;
       int age;
       int marks1;
       int marks2;
       person(string n,int a,int m1,int m2)
       {
        name=n;
        age=a;
        marks1=m1;
        marks2=m2;
       }
       void hello()
       {
        cout<<name<<" "<<age<<endl;
       }
       int total()
       {
        return marks1+marks2;
       }

};
int main()
{
    person Rijuan("Rijuan Monju",21,80,85);
    Rijuan.hello(); //eibve function teke obj call korte pari
    cout<<Rijuan.total()<<endl; //function teke obj call kirte pari
     
    return 0;
}