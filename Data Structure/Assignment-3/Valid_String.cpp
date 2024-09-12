#include <bits/stdc++.h>
using namespace std;

bool validString(string& s) 
{
    stack<char> st;

    for (char c : s) 
    {
         if (!st.empty() && c == 'A' && st.top() == 'B')
        {
            st.pop();
        } 
        else if (!st.empty() && c == 'B' && st.top() == 'A') 
        {
            st.pop();
        } 
        else 
        {
            st.push(c);
        }
    }
    return st.empty();
}

int main() 
{
    int T;
    cin >> T;

    while (T--) 
    {
        string s;
        cin >> s;

        if (validString(s)) 
            cout << "YES" << endl; 
        else 
            cout << "NO" << endl;
    }

    return 0;
}
