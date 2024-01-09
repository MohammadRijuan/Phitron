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
    for (int i = 0; i < 2; i++)// i< 2 ata holo i<n-1
    {
        for (int j = i+1; j < 3; j++)
        {
            if(a[i].marks>a[j].marks) //coto teke boro..bor teke coto chaile a[i].marks<a[j].marks hbe
            {
                swap(a[i],a[j]);
            }
        }      
    }
    for (int i = 0; i < 3; i++)
    {
        cout<<a[i].name<<" "<<a[i].roll<<" "<<a[i].marks<<endl;
    }
    
    
return 0;
}