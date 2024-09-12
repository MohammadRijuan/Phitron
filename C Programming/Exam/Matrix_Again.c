#include <stdio.h>

int main()
{
    int N, M;
    scanf("%d %d", &N, &M);

    int a[N][M];
    for (int i = 0; i < N; i++) 
    {
        for (int j = 0; j < M; j++) 
        {
            scanf("%d", &a[i][j]);
        }
    }
    //row
    int r=N-1;
    for (int j = 0; j < M; j++) {
        printf("%d ", a[r][j]);
    }
    printf("\n");

    //col
    int c=M-1;
    for (int i = 0; i < N; i++) {
        printf("%d ", a[i][c]);
    }

    return 0;
}
