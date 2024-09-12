(a)problem-1


int count = 0;
for (int i = n; i > 0; i /= 2)
{
    for (int j = 0; j < n; j+=5)
   {
        count += 1;
    }
}

Answer : O(nlongn)


(b)problem-2


for(int i =1; i*i<n; i++)
{
     cout << “hello”;
}


Answer : O(sqrt(n))


(c)problem-3


for(int i =1; i<n; i=i*2)
{
   for(int j=1; j*j<n; j+=2)
  {
      cout << “hello”;
   }
}

Answer : O(logn*sqrtroot(n))


(d)problem-4
int m = 1;
for(int i=0; m<=n; i++)
{
    m+=i;
}

Answer : O(n)