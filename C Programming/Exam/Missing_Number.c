
#include <stdio.h>

int main() 
{
    int T;
    scanf("%d", &T); 

    for (int i = 0; i < T; i++) 
    {
        int S, A, B, C;
        scanf("%d %d %d %d", &S, &A, &B, &C);
        int missing = S - (A + B + C); 
        printf("%d\n", missing); 
    }

    return 0;
}
