#include<bits/stdc++.h>
using namespace std;
int main()
{
    /* list<int>mylist={10,20,30};
    list<int>newlist;

    //newlist=mylist;
    newlist.assign(mylist.begin(),mylist.end());
    for(int val : newlist)
    {
        cout<<val<<endl;
    }*/

    /*list<int>mylist={10,20,30};
    mylist.push_back(100);  //pichone tail e jog hbe
    mylist.push_front(100);  //samne head e jog hbe 
    mylist.pop_back();  //pichon teke delete hobe
    mylist.pop_front();  //samne delete hobe
    
    for(int val : mylist)
    {
        cout<<val<<endl;
    }*/

    /*list<int>mylist={10,20,30,40};
    mylist.insert(next(mylist.begin(),2),100);
    for(int val : mylist)
    {
        cout<<val<<endl;
    }*/

    /*list<int>mylist={10,20,30,40,50};
    mylist.erase(next(mylist.begin(),2));
    mylist.insert(next(mylist.begin(),3),{100,200,300});
    for(int val : mylist)
    {
        cout<<val<<endl;
    }*/

    /*list<int>mylist={10,20,30,40,50,60,70};
    mylist.erase(next(mylist.begin(),2),next(mylist.begin(),5));
    for(int val : mylist)
    {
        cout<<val<<endl;
    }*/

    /*list<int>mylist={10,20,30,40,30,30,70};
    replace(mylist.begin(),mylist.end(),30,100);
    for(int val : mylist)
    {
        cout<<val<<endl;
    }*/

    list<int>mylist={10,20,30,40,30,30,70};
    auto it=find(mylist.begin(),mylist.end(),40);
    //cout<<*it<<endl;
    if(it==mylist.end())
    {
        cout<<"not found";
    }
    else
    {
        cout<<"found";
    }




     
    return 0;
}