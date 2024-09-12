#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>v;
    //cout<<v.max_size()<<endl;

    /* cout<<v.capacity()<<endl; //capacity over hoye gele seta 1 1 kore bare na..double kore fele..push back function size barate kaj kore..
    v.push_back(10);
    cout<<v.capacity()<<endl;
    v.push_back(20); 
    cout<<v.capacity()<<endl;
    v.push_back(30); 
    cout<<v.capacity()<<endl;
    v.push_back(40); 
    cout<<v.capacity()<<endl;
    v.push_back(50);
    cout<<v.capacity()<<endl; */


    /* v.push_back(10); 
    v.push_back(20); 
    v.push_back(30); 
    v.push_back(40); 
    v.push_back(50);
    v.clear();  // v.clear() function size clear kore garbage value dey...but memory delete korte pare na..
    cout<<v.size()<<endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    }
    cout<<v[0]<<endl; */

    v.push_back(10); 
    v.push_back(20); 
    v.push_back(30); 
    v.push_back(40); 
    v.push_back(50);
    //v.resize(2); //v.resize(2) dile output 10 20 dibe
    v.resize(7); //v.resize(2) r v.resize (7) eksathe dile 10 20 er por baki 5ta garbage value dibe
    cout<<v.size()<<endl;
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    } 
    
     
    return 0;
}