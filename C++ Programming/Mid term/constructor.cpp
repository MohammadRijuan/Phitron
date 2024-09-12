#include<bits/stdc++.h>
using namespace std;
class person
{
    public :
        char name[100];
        float height;
        int age;
        
        person(int a, float h,char* n)
        {
            age=a;
            height=h;
            strcpy(name,n);
        }
};
int main()
{
    person rijuan( 26 ,5.6,"Rijuan Monju");
    person intisar( 25 ,5.5,"Intisar Nibraj");
    if(rijuan.age<intisar.age)
    {
        cout<<"Intisar"<<endl;
    }
    else{
        cout<<"Rijuan";
    }
    
     
    return 0;
}