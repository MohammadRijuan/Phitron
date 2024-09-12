#include<stdio.h>
void fun (int *p)
{
    *p=50;
    printf("fun p er value -%d\n",*p);
    printf("fun p er address -%p\n",&*p);
}

int main()
{
    int x=10;
    fun(&x);
    printf("main x er value -%d\n",x);
    printf("main x er address -%p",&x);

    return 0;
}