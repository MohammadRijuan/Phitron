#include <stdio.h>
#include<string.h>

int main() 
{
    char str[1001];
    fgets(str, sizeof(str), stdin);

    int capitalCount = 0;
    int smallCount = 0;
    int spaceCount = 0;

    for (int i = 0; str[i] != '\0'; i++) 
    {
        if (str[i] >= 'a' && str[i] <= 'z') 
        {
            smallCount++;
        } 
        else if (str[i] >= 'A' && str[i] <= 'Z') 
        {
            capitalCount++;
        } 
        else if (str[i] == ' ') 
        {
            spaceCount++;
        }
    }

    printf("Capital - %d\n", capitalCount);
    printf("Small - %d\n", smallCount);
    printf("Spaces - %d\n", spaceCount);

    return 0;
}
