#include<stdio.h>
void fun ( int i)
{
    if(i==6) return; //base cae
    //desire output porjnto pawar jonno recursion infnite loop thamanor jonno base case use kora
    printf("%d\n",i);
    fun(i+1);
}
int main()
{
     fun(1);
    return 0;
}