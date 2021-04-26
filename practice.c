#include<stdio.h>

int main(){
    int i=1, sum=0, n;
    printf("enter value of n\n");
    scanf("%d",&n);
    while (i<=n)
    {
        sum+=i;
        i++;
    }
    printf("the value is %d",sum);
    return 0;
}