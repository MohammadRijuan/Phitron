#include<bits/stdc++.h>
using namespace std;
int main()
{
    vector<int>arr;
    int n;
    cin>>n;

    for (int i = 0; i < n; i++)
    {
        int x;
        cin>>x;
        arr.push_back(x);
    }

    int k;
    cin>>k;

    int l = 0;
    int r = n;

    while (l <= r)
    {
        int mid = (l + r) / 2;
        if (arr[mid] == k)
        {
            cout << mid << endl;
            break;
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
    if (l > r)  
    {
        cout << "Not Found" << endl;
    }


    return 0;
}