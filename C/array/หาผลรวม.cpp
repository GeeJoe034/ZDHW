#include <stdio.h>


int main()
{
    int sum=0,j,i,max;
    int myNumber[50];
    printf("Enter Num:");
    scanf("%d",&j);
    for  (i = 1; i < j; i++)
    {
        myNumber[i] = i;
        sum = sum + myNumber[i];
     
    }
    printf("Sum of 1 to %d is : %d\n",j,sum);
    return 0;
}

