#include<iostream>
#include<utility> //swap er header file..tkn & use na korley hbe
using namespace std;
//void my_swap(int *a,int *b) //jodi pointer use na kortam tahole man gulo peto na
//{
//    int tmp=*a;
//    *a=*b;
//    *b=tmp;
///}
int main()
{
    int a,b;
    cin>>a>>b;
    swap(a,b); //jodi & na ditam tahole atar man rcv korte parto na
    cout<<a<<" "<<b;


    return 0;
}