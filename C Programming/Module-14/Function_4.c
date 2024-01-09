#include<stdio.h>
//no return + no parameter
//reeturn r parametr o nai tai void use korlam
void sum(void)
{
    int a,b;
    scanf("%d %d",&a,&b);
    int s=a+b;
    printf("%d\n",s);
}
int main()
{
    sum();
    sum();
    //sum diye function call korlam main er vetor nahole code run hbena
     
    return 0;
}