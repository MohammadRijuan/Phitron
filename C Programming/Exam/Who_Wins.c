#include <stdio.h>

int main() {
    int N;
    scanf("%d", &N);
    int tiger = 0, pathan = 0;

    for (int i = 0; i < N; i++) 
    {
        int X1, X2;
        scanf("%d %d", &X1, &X2);
        if (X1 > X2) 
        {
            tiger++;
        } 
        else if (X2 > X1) 
        {
            pathan++;
        }
    }

    if (tiger > pathan) 
    {
        printf("Tiger\n");
    } 
    else if (tiger < pathan) 
    {
        printf("Pathan\n");
    } 
    else 
    {
        printf("Draw\n");
    }

    return 0;
}
