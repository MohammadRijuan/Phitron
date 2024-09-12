#include<stdio.h>
int main()
{
    int x=100;
    //printf("%p\n",&x);
    int* p=&x;
    //printf("%p\n",p);
    //dereferrence
    //printf("%p\n",*p);
    *p=500;
    printf("%d",x);

    return 0;
}
//pointer holo original chabir nokol chabi...
// %p diye address lika hoy