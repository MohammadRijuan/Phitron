#include<bits/stdc++.h>
using namespace std;
int main()
{
    /* vector <int>  x={10,20,30};
    vector <int> v={1,2,3}; 
    v=x; //O(N)
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    } */

    /* vector <int>  x={10,20,30,40}; //output 10  20 30 40  50 e asbe bcoz size same na tai...
    vector <int> v={1,2,3}; 
    v=x; //O(N)
    for (int i = 0; i < v.size(); i++)
    {
        cout<<v[i]<<" ";
    } */

    vector <int>  x={10,20,30,40};
    x.pop_back(); //pop back function last er dik teke element remove kore
    for (int i = 0; i < x.size(); i++)
    {
        cout<<x[i]<<" ";
    }
    
    return 0;
}