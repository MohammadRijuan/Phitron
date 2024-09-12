#include<stdio.h>
//global
int x=500;
void fun(void)
{
    printf("fun address - %p\n",&x);
}
int main()
{
    printf("main address - %p\n",&x);
    fun();
     
    return 0;
}