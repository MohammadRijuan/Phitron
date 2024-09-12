#include<stdio.h>
void hurr( int n)
{
    if(n==0) return;
    int x=(n%10);
    hurr(n/10);
    printf("%d ",x);
}
int main()
{
    int test;
    scanf("%d",&test);
    for (int t = 0; t < test; t++)
    {
        int n;
        scanf("%d",&n);
        hurr(n);
        if (n==0)
        {
            printf("0");
        }
        
        printf("\n");
        
    }
    return 0;
}