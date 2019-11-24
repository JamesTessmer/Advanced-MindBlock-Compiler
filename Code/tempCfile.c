#include <stdio.h>
#include <string.h> 
void pp(); 
int main(); 
int x;
char ppp[50];
int abc;
void pp(){
printf("Please enter a value for x  \n"); 
scanf("%d", &x); 
}
int main(int argc, char * argv[]){
strcpy(ppp,"Test"); 
printf("%s  \n",ppp); 
x=15;
pp(); 
printf("103020 + %d  \n",x); 
abc=20;
if(x<abc){
x=x+1;
}else{}
while(x<abc){
x=x+1;
printf("X is less than abc  \n"); 
}
return 0; 
}
