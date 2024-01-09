#include<bits/stdc++.h>
using namespace std;
class person 
{
    public :
       string name ;
       int age;
       person(string name,int age)
       {
        this->name=name;
        this->age=age;
       }

};
int main()
{
    person* Rijuan= new person("Rijuan monju",21);
    person* Intisar=new person("Intisar nibraj",25);
    //Rijuan=Intisar; //eibaveo kora jabe amar name nibrajer name copy hbe;
   //Rijuan->name=Intisar->name;
    //Rijuan->age=Intisar->age;
    *Rijuan=*Intisar;
    delete Intisar;
    cout<<Rijuan->name<<" "<<Rijuan->age<<endl;
     
    return 0;
}