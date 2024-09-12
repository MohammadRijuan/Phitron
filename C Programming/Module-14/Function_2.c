#include<stdio.h>

//return+no parameter
int sum()
{
    int a,b;
    scanf("%d %d",&a,&b);
    int s=a+b;
    return s;
}
int main()
{
    int s=sum();
    printf("%d",s);
     
    return 0;
}