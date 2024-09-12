//no return + no parameter
#include<stdio.h>
void sum(void)
{
    int a,b;
    scanf("%d %d",&a,&b);
    int sum=a%b;
    printf("Answer is: %d",sum);
}
int main()
{
    sum();    
    return 0;
}