#include<stdio.h>
int main()

{
    int n,i;
    scanf("%d",&n);
    if(i<=0)
    {
        for ( i = n; i >0; i++)
        {
            printf("%d",i);
        }
    }
    else
    {
        for(i=1;i<=n;i--)
        {
            printf("%d",i);
        }
    }
    
    
    return 0;
}
