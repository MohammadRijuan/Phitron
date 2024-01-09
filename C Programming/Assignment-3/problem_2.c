#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);

    for (int i = 1; i <= n; i++) 
    {
        int s=n-i;
        for (int j = 1; j <= s; j++) 
        {
            printf(" ");
        }
        for (int j = 1; j <= i; j++) {
            printf("%d", i);
        }
        printf("\n");
    }
    return 0;
}
