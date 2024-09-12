#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long t;
    cin>>t;

    while(t--)
    {
        long long n,count_one=0,flag=0;
        cin>>n;
        vector<long long>v(n);

        for (int i = 0; i < n; i++)
        {
            cin>>v[i];

            if(flag==0 && v[i]==1)
            {
                count_one++;
            }
            else flag++;
        }
        if((n==count_one && count_one% 2 !=  0) || (n!=count_one && count_one%2 == 0))
        {
            
            cout<<"First"<<endl;
        }
        else
        {
            cout<<"Second"<<endl;
        }

    } 
    return 0;
}