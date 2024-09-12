#include<bits/stdc++.h>
using namespace std;
int main()
{
    //vector<int>v; //type-1

    /* vector<int>v(5); //type-2
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl; */
    
    /* vector<int>v(5,10);   //10 diye value input korlam //type-3

    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl; */

    /* vector<int> v2(5,100); //type-4
    vector<int>v(v2);  //vector v2 vector er element copy korlo

    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl; */

    /* int a[6]={1,2,3,4,5,6};
    vector <int> v(a,a+6); // type-5 (a) array er suru (a+6) array er ses 
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl; */
    
    /* vector <int> v = {2,10,3};
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<endl; */

    vector<int> v;
    v[2]=100; // eibave value nite parbona karon size e create hoini

    cout<<v.size()<<endl;

    return 0;
}