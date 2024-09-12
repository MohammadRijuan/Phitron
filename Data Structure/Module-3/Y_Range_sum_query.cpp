/* #include<bits/stdc++.h>
using namespace std;
int main()
{
    int n,q;
    cin>>n>>q;
    int a[n];
    for (int i = 0; i < n; i++) //O(N)
    {
        cin>>a[i];
    }
    while(q--) //O(q) jaa 10 to the power 5
    {
        int l,r;
        cin>>l>>r;
        l--;
        r--;
        int sum=0;
        for (int i = l; i <= r; i++) //O(n)
        {
            sum+=a[i];
        }
        cout<<sum<<endl; //O(q*n)
    }
    return 0;
    //ei process ta codeforces e required tym er besi hye jacce 10 to the power 10 asce..kintu amr tym limit 10 to the power 5....time limit kacce..
} */


//prefix sum diye korbo (range related)- 9,10 er kromojojito sonka er moto
#include<bits/stdc++.h>
using namespace std;
int main()
{
    long long n,q;
    cin>>n>>q;
    long long a[n];
    for (int i = 0; i < n; i++)
    {
        cin>>a[i];
    }
    long long pre[n];
    pre[0]=a[0]; // index 0 er man nij tekey korte hbe
    for (int i = 1; i < n; i++)
    {
        pre[i]=a[i]+pre[i-1];
    }
    /* for (int i = 0; i < n; i++)
    {
        cout<<pre[i]<<" "; //kromojojito hcce kina check kora just..ata aladha vabe deka tik ase kina
    } */

    while (q--)
    {
        long long l,r;
        cin>>l>>r;
        l--;
        r--;
        long long sum;
        if(l==0) sum=pre[r];
        else sum=pre[r]-pre[l-1];
        cout<<sum<<endl;
    }
    
    
    return 0;
}