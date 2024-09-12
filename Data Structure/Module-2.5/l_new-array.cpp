#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    vector<int>A(n); //vector diyr a nilam 
    vector<int>B(n);  //vector diye b nilam
    for (int i = 0; i < n; i++)
    {
        cin>>A[i];
    }
    for (int i = 0; i < n; i++)
    {
        cin>>B[i];
    }
    vector<int>C=B; //b vector c te nilam
    C.insert(C.end(),A.begin(),A.end());
    for (int i = 0; i < C.size(); i++)
    {
        cout<<C[i]<<" ";  //array c te print korlam
    }
    return 0;
}