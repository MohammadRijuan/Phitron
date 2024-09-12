#include<stdio.h>
int main()
{
    double x=5.26;
    double *ptr=&x;
    double *ptr2=ptr;
    *ptr=100.20;
    printf("x er address - %0.2lf\n",x);
    printf("ptr er address - %0.2lf\n",*ptr);
    //printf("ptr er size - %d\n",sizeof(ptr));
    return 0;
}