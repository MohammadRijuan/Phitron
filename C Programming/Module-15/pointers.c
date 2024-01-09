#include<stdio.h>
int main()
{
    int x=100;
    int *ptr= &x;
    printf("x er address -%p\n",&x);
    printf("ptr er address -%p\n",ptr);
    printf("*ptr er address -%p\n",*ptr);
    //derefference
    *ptr=500;
    printf("%d",*ptr);


    return 0;
}