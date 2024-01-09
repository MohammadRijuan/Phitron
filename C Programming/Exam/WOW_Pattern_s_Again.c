#include<stdio.h>
int main()
{
    int N;
    scanf("%d",&N);
    for (int i = 1; i <= N; i++)
    {
        for (int j = 1; j <= N-i; j++)
        {
            printf(" ");
        }
        for (int j = 0; j <= 2*i-2; j++)
        {
            if(i%2==0)
            {
                printf("*");
            }
            else{
                printf("^");
            }
            
        }
        printf("\n");
        
        
    }
     
    return 0;
}