#include<bits/stdc++.h>
using namespace std;
namespace Rijuan
{
    int age=21;
    void hello()
    {
        cout<<"Rijuan namespaces"<<endl;
    }
}
namespace Intisar
{
    int age2=24;
    void hello2()
    {
        cout<<"Intisar namespaces"<<endl;
    }
}
using namespace Rijuan;
using namespace Intisar;
int main()
{
    cout<<age<<endl;
    hello();
    Intisar::hello2();
    //cout<<age2<<endl;
    
    return 0;
}