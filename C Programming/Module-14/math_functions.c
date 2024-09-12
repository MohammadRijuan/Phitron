#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main()
{
    //double x;
    //scanf("%lf",&x);
    //int ans=ceil(x);
    //int ans=floor(x);
    //int ans=round(x);

    //double x;
    //scanf("%lf %lf",&x);
    //double ans=sqrt(x);
    //double a,b;
    //scanf("%lf %lf",&a,&b);
    //double ans=pow(a,b);
    //printf("%lf",ans);
    int x;
    scanf("%d",&x);
    int ans=abs(x);
    printf("%d",ans);


    return 0;
}
//(ceil) builtin function hisebe kaj kore jodi doshomiker por .01 o thake tahole ans porer songka de jemon 3.01 er output 4 dibe
//(floor) o same as biltin function jdi 3.01 thake tahole 3 e ans dibe...
//same as (round) jodi 3.49 thake output 3 dibe jodi 3.5er besi thake tahole 4dibe output
//(sqrt) root er man dey 25 thakle ans 5dibe...21 thakle 4 dibe...jodi (double e ni exact man dibe r 0.2 or something dile doshomiker por joto gor chai ta pabo)
//(sqrt) e ans int e rakle exact man asena..double edite hoy
//|(pow) poer er kaj kore
//(abs) positive hok or neg sob guloke pos e convert kore