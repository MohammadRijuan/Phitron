#include<bits/stdc++.h>
using namespace std;

int find_duplicate(vector<int>&arr,int k)
{
    
    int l = 0;
    int r = arr.size()-1;
    int count;

    while (l <= r)
    {
        int mid = (l + r) / 2;

        if (arr[mid] == k)
        {
            count=mid;
            r=mid-1;
        }

        else if (arr[mid] < k)
        {
            l = mid + 1;
        }

        else
        {
            r = mid-1;
        }
    }
    return count;
    
}
int main()
{
    int n;
    cin>>n;

    vector<int>arr(n);

    for (int i = 0; i < n; i++)
    {
        cin>>arr[i];
    }
    int k;
    cin>>k;

    int ans=find_duplicate(arr,k);

     if (arr[ans + 1] == k)
    {
        cout << "YES" << endl;
    }
    else
    {
        cout << "NO" << endl;
    }


    return 0;
}