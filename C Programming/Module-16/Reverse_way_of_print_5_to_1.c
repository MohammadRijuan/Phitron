#include<stdio.h>
void fun( int i)
{
    if (i==6) return; //base case
    fun(i+1); //recursion k aghe print korar aghe call korle reverse way te print kore..
    printf("%d\n",i);

}
int main()
{
     fun(1); //1 k aghe print kore reverse way te 5 porjnto
    return 0;
}