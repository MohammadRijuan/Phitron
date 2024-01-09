#include <stdio.h>

int main() 
{
    int N;
    scanf("%d", &N);

    int a[N];
    for (int i = 0; i < N; i++) 
    {
        scanf("%d", &a[i]);
    }

    int h_mark = a[0];
    for (int i = 1; i < N; i++) 
    {
        if (a[i] > h_mark) 
        {
            h_mark = a[i];
        }
    }

    for (int i = 0; i < N; i++) 
    {
        int difference = h_mark - a[i];
        printf("%d ", difference);
    }

    return 0;
}
