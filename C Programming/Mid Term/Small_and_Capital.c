#include<stdio.h>
#include<string.h>
int main()
{
    char s;
    int small=0,capital=0;
    while (scanf("%c", &s) != EOF)
    {
        if(s >='a' && s <='z')
        {
            small++;
        }
        else
        {
            capital++;
        }
    }
    printf("%d %d",capital,small);


    return 0;
}