#include<stdio.h>
//no_return +parameter
//void mane holo no return
//kono_reeturn type na thakle amra void likhi
//void thakle_reeturn likte parbo kintu kono man dewa jbe na
void sum(int x,int y)
{
    int s=x+y;
    printf("%d",s);
}

int main()
{
    int a,b;
    scanf("%d %d",&a,&b);
    sum(a,b);
     
    return 0;
}