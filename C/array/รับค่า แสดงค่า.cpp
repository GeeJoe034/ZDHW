#include <stdio.h>
#include <stdlib.h>
int main() {
int months[12]={0.0};
int j,i;
printf("Cost of the Years\n");
for(i=0; i<12; i++){
printf("Enter of month %d :",i+1);
scanf("%d",&months[i]); }
for(i=0; i<12; i++){
printf("\nMonths %d is %d",i+1,months[i]);
}
return 0;
}