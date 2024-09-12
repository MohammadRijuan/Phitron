#include<stdio.h>
int main()
{
    long long int sum=0;
    int i;
    int n;
    scanf("%d",&n);
    for( i=1; i<=n; i=i+1 )
    {
        sum+=i;
    }
    printf("%lld\n",sum);
    return 0;
}

//n songkok prjonto jog korar ketre ei method hobe//