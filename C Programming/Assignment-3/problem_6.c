#include<stdio.h>
void fun ( int x)
{
    x=150;
    printf("fun x er address - %p\n",&x);

}
int main()
{
    int x=50;
    printf("main x er address - %p\n",&x);
    fun(x); 
    printf("main x er value - %d\n",x);
     
    return 0;
}