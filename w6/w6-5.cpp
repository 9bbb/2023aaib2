#include <stdio.h>

int main( void )
{
   int i,j;
   int n;

   printf("請輸入大小:");
   scanf("%d",&n);
   printf("\n");
	for(i=1;i<=n;i++){
		for(j=1;j<=i;j++)
			printf(" ");
		for(j=1;j<=n;j++)
			printf("*");
		printf("\n");
		}

   return 0;
}
