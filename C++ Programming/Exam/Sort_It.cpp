#include<bits/stdc++.h>
using namespace std;
class student 
{
    public :
     string nm;
     int cls;
     char s;
     int id;
     int math_marks;
     int eng_marks;
     int total_marks;

};

bool order(student a,student b)
{
    if(a.total_marks==b.total_marks) return a.id<b.id ;
    else return a.total_marks > b.total_marks;

}
int main()
{
    int n;
    cin>>n;
    student obj[n];
    for (int i = 0; i < n; i++)
    {
        cin>>obj[i].nm;
        cin>>obj[i].cls;
        cin>>obj[i].s;
        cin>>obj[i].id;
        cin>>obj[i].math_marks;
        cin>>obj[i].eng_marks;
        cin.ignore();
        obj[i].total_marks=obj[i].math_marks+obj[i].eng_marks;
    }
    sort(obj,obj+n,order);
    for (int i = 0; i < n; i++)
    {
        cout<<obj[i].nm<<" "<<obj[i].cls<<" "<<obj[i].s<<" "<<obj[i].id<<" "<<obj[i].math_marks<<" "<<obj[i].eng_marks<<endl;
    } 
     
    return 0;
}