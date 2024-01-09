#include<stdio.h>
int main()
{
    int row,col;
    scanf("%d %d",&row,&col);
    int a[row][col];
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            scanf("%d",&a[i][j]);
        }
    }
    //int r; //exact row
    //scanf("%d",&r);
    //for (int i = 0; i < col; i++)
    //{
        //printf("%d ",a[r][i]);
        
    //}
    int c; //exact column
    scanf("%d",&c);
    for (int i = 0; i < row; i++)
    {
        printf("%d\n",a[i][c]);
    }
    
    printf("\n");
}