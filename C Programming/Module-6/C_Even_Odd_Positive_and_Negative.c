#include<stdio.h>
int main()
{
     int n;
     scanf("%d",&n);
     int i,a;
     
     int even=0,odd=0,pos=0,neg=0;
     
     for ( i = 1; i <=n; i++)
     
     {
        scanf("%d",&a);
        if(a%2==0)
        {
            even=even+1;
            //printf("%d\n",a);
        }
        else
        {
            odd=odd+1;
        }
        if(a>0)
        {
            pos=pos+1;
        }
         else if(a<0)
        {
            neg=neg+1;
            //printf("%d\n",a);
        }
     }
        printf("Even: %d\n Odd: %d\n Positive: %d\n Negative: %d\n",even,odd,pos,neg);
     
     
    return 0;
}