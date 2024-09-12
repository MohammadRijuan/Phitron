#include<bits/stdc++.h>
using namespace std;

class student
{
    public:
    string name;
    int roll;
    int marks;

    student(string name,int roll,int marks)
    {
        this->name=name;
        this->roll=roll;
        this->marks=marks;
    }
};

class cmp
{
    public:
        bool operator()(student a, student b)
        {
            if(a.marks < b.marks)
            {
                return true;
            }
            else if(a.marks > b.marks) return false;
            
            else if(a.marks == b.marks)
            {
                if(a.roll > b.roll) return true;
                else if(a.roll == b.roll) return true;
                else if(a.roll < b.roll) return false;
            }
            return false;

        }
};
int main()
{
    int n;
    cin>>n;
    priority_queue<student,vector<student>,cmp>pq;

    for (int i = 0; i < n; i++)
    {
        string name;
        int roll;
        int marks;

        cin>>name>>roll>>marks;
        student obj(name,roll,marks);
        pq.push(obj);
    }

    int q;
    cin>>q;

    while(q--)
    {
        int i;
        cin>>i;

        if(i==0)
        {
            string name;
            int roll,marks;
            
            cin>>name>>roll>>marks;
            
            student stdnt(name,roll,marks);

            pq.push(stdnt);
            
            if(pq.empty()) cout<<"Empty"<<endl;
            else
            cout<<pq.top().name<<" "<<pq.top().roll<<" "<<pq.top().marks<<endl;
        }

        else if(i==1)
        {
            if(pq.empty()) cout<<"Empty"<<endl;
            
            else
            cout<<pq.top().name<<" "<<pq.top().roll<<" "<<pq.top().marks<<endl;
        }

        else if(i==2)
        {
            if(pq.empty()) cout<<"Empty"<<endl;
            
            else
            {
                pq.pop();
                
                if(pq.empty()) cout<<"Empty"<<endl;
                else
                cout<<pq.top().name<<" "<<pq.top().roll<<" "<<pq.top().marks<<endl;
            }

        }
        else
        {
            break;
        }
    }
    
     
    return 0;
}
