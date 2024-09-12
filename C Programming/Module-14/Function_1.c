#include<stdio.h>
//return+parameter


int sum(int x,int y)
{
    int sum=x+y;
    return sum;
}
int main()
{
    //int s=sum(10,20);
    //printf("%d",s);
    //s e nilam jate output hariye na jai

    //onno way te print kora jai

    printf("%d\n",sum(10,20));
    printf("%d",sum(100,200));

    //arekta way

    //int x,y;
    //scanf("%d %d",&x,&y);
    //printf("%d",sum(x,y));
    
    return 0;
}