#include<stdio.h>
int main()
{
    int a;
    scanf("%d",&a);
    if(a>=0)
    {
        if(a>0)
        {
          printf("positive");  
        }
        else
        {
            printf("zero");
        }
    }
    else
    {
        printf("negative");
    }   

    return 0;
}