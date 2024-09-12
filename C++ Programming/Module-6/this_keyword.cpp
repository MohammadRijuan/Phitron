#include<bits/stdc++.h>
using namespace std;
class person
{
    public :
      string name;
      int age;
      person(string name,int age)
      {
        (*this).age=age;// ei 2 bave nite pari.. this ekta pointer er moto kaj kore

        this->name=name;
      }
      void hello()
      {
        cout<<"hello"<<endl;
      }


};
int main()
{
    person Rijuan("Rijuan Monju",21);
    cout<<Rijuan.name<<" "<<Rijuan.age<<endl;
     
    return 0;
}