#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector <int> v={1,2,3,4,5};
    //v.erase(v.begin()+3); //3no index er value remove kore output asbe 1 2 3 5
    v.erase(v.begin()+1 , v.begin()+4); //1no index teke 4no index porjonto muche felbe 
    for(int x: v)
    {
        cout<<x<<" ";
    } 
    return 0;
}