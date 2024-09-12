#include<stdio.h>
void good(int *b)
{
    //printf("main x er value- %d\n",*b);
    *b=20;
    printf("b er value- %p\n",b);
}
int main()
{
    int x=10;
    printf("x er address- %p\n",&x);
    good(&x);
    printf("x er value- %d\n",x);

    return 0;
}