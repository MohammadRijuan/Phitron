#include<bits/stdc++.h>
using namespace std;
class student 
{
    public :
      string name;
      int roll;
      int marks;
};
int main()
{
    student a[3]; //class e constructor nilam na karon constructor array te sob nite parena
    for (int i = 0; i < 3; i++)
    {
        getline(cin,a[i].name);// cin e name nile gapla hcce tai getline e nilam
        cin>>a[i].roll>>a[i].marks;
        cin.ignore(); //r enter pblm issue solve krte cin.ignore nilam
    }
    student mx;
    mx.marks=INT_MIN;
    for (int i = 0; i < 3; i++)
    {
        if(a[i].marks>mx.marks)
        {
            mx=a[i];
        }
    }
    cout<<mx.name<<" "<<mx.roll<<" "<<mx.marks<<endl;

    student mn;
    mn.marks=INT_MAX;
    for (int i = 0; i < 3; i++)
    {
        if(a[i].marks<mn.marks)
        {
            mn=a[i];
        }
    }
    cout<<mn.name<<" "<<mn.roll<<" "<<mn.marks<<endl;
     
    return 0;
}