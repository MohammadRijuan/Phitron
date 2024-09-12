//no return+parameter
#include<stdio.h>
void sum(int x,int y)
{
    int s=(x*x)-y;
    printf("answer is: %d",s);
    return;
}

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    sum(a,b);
     
    return 0;
}