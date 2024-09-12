//return+parameter
#include<stdio.h>
int sum(int x, int y)
{
    int sum=x*y;
    return sum;
}
int main()
{
    printf("Answer is: %d",sum(5,8));
     
    return 0;
}