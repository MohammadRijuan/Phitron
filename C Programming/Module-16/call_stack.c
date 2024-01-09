#include<stdio.h>
void world()
{
    printf("world start\n");
    printf("world end\n");


}
void Hello()
{
    printf("hello start\n");
    world();
    printf("hello end\n");

}
int main()
{
    printf("main start\n");
    Hello();
    printf("main end\n");
     
    return 0;
}