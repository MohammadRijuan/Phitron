#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;

    while(t--)
    {
        map<int,int>ar;
        int n;
        cin>>n;
        for (int i = 0; i < n; i++)
        {
            int x;
            cin>>x;
            ar[x]++;
        }
        int max=INT_MIN;

        for (auto it = ar.begin(); it!= ar.end(); it++)
        {
            if(it->second > max)
            {
                max=it->second;
            }
        }

        int max_number=INT_MIN;

        for (auto it = ar.begin(); it!= ar.end(); it++)
        {
            if(it->second == max)
            {
                if(it->first > max_number)
                {
                    max_number=it->first;
                }
            }
        }  
        cout<<max_number<<" "<<max<<endl; 

    } 
    return 0;
}