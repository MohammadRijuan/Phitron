#include<bits/stdc++.h>
using namespace std;
int main()
{
    map<string,int>mp;  //map always 2vabe input kore insert r pair kore
    /* mp.insert({"sakib",75}); 
    mp.insert({"tamim",19}); 
    mp.insert({"samim",79}); 
    mp.insert({"rahat",100}); */

    /*for (auto it = mp.begin(); it!= mp.end(); it++)
    {
        cout<<it->first<<" "<<it->second<<endl; //map always elomelo vabe output dey
    }*/

    // cout<<mp["rahat"]<<endl;  //rahat er value dibe

    // cout<<mp["akib"]<<endl; //jeta nai setar value 0 dibe

    /* if(mp.count("akib"))
    {
        cout<<"ase"<<endl;
    }
    else
    cout<<"nai"<<endl; */

    mp["sakib"]=75;  //eibaveo newa jabe
    mp["tamim"]=19;
    mp["rahat"]=100;
    mp["samim"]=79;

    for (auto it = mp.begin(); it!= mp.end(); it++)
    {
        cout<<it->first<<" "<<it->second<<endl; //map always elomelo vabe output dey
    }
     
    return 0;
}