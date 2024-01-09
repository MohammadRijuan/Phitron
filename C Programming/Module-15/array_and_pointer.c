#include<stdio.h>
int main()
{
    int ar[5]={10,20,30,40,50};
    //printf("0th array er address -%p\n",&ar[1]); 
    //printf("0th array er address -%p\n",ar); 
    //printf("0th array er value -%d\n",ar[0]); 
    //printf("0th array er value -%d\n",*ar);

    //printf("0th array er value -%d\n",ar[1]);
    //printf("0th array er value -%d\n",*(ar+1));
    
    //onek upaye likha jai

    printf("0th array er value -%d\n",ar[1]);
    printf("0th array er value -%d\n",*(1+ar));
    printf("0th array er value -%d\n",1[ar]);
    printf("0th array er value -%d\n",*(ar+1));


    return 0;
}