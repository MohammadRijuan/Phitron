#include<bits/stdc++.h>
using namespace std;
int main()
{
    //type -1

    /* vector <int> v={1,2,2,3,4,5,1,2,4,5,3,2};
    //cout<<find(v.begin(),v.end(),3); //ata korle error dibe
    vector <int> :: iterator it; //iterator holo ekta pointer .iterator ke print korle er address pawa jabe..iterator er value pete iterator ke de-referrence (*it) korle er value pawa jabe
    it = find (v.begin(),v.end(),3);
    cout<<*it; */

    vector <int> v={1,2,2,3,4,5,1,2,4,5,3,2};
    auto it =find(v.begin(),v.end(),3); //auto dile vector detect korte pare.. 
    //cout<< *it ;

    if(it == v.end())
    {
        cout<<"Not found";
    }
    else cout<<"found";


    return 0;
}
