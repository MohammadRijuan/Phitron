#include <bits/stdc++.h>
using namespace std;

int main()
{
  queue<string>q;  
  int Q;
  cin >> Q;
  
  while(Q--)
    {
      int a;
      cin >> a;
      if(a == 0)
      {
        string s;
        cin >> s;
        q.push(s);
      }
      else
      {
        if(!q.empty())
        {
          cout << q.front() << endl;
        q.pop();
        }
        else
        {
          cout << "Invalid" << endl;
        }
      }
    }
}