#include<stdio.h>
void fun ( int x)
{
    x=200;
    //printf("fun x er address -%p\n",&x);

}
int main()
{
    int x=10;
    //printf("main x er address -%p\n",&x);
    fun(x);
    printf("main x er value -%d\n",x);
     
    return 0;
}
//jhetu main ey variable declare kora ache tahole tokon baki function er kono kicu jai asena
