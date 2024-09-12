#include<bits/stdc++.h>
using namespace std;
int main() 
{
    int n;
    cin>>n;
    int mid=n/2;

    for (int i = 0; i<n; i++) 
    {
        for (int j = 0; j<n; j++) 
        
        {
            if(i==j && i!= mid) 
            {
                cout <<"\\";
            } 
             
            else if(i==j && i==mid)
            {
                cout<<"X";
            }
            else if(j== n-1-i) 
            {
                cout<<"/";
            }
            else 
            {
                cout<<" ";
            }
        }
        cout<<endl;
    }

    return 0;
}
