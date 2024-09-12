#include<stdio.h>
int main(){
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        for(int j=1;j<=n;j++){
            if(i==(n+1)/2){
                if(j==(n+1)/2){
                    printf("X");
                }
                else{
                    printf("*");
                }
            }
            else if(j==i){
                printf("\");
            }
            else if(j==(n+1-i)){
                printf("/");
            }
            else{
                printf("*");
            }
           

        }
      printf("\");
    }
    return 0;
