#include <stdio.h>
#include <string.h>
int main(int argc, char const *argv[])
{
	printf("enter the input =\n");
	char s[100];
	scanf("%[^\n]",s);
	/*getchar();*/
	/*scanf("%c",&s);*/
	/*int x ;*/
	/*x = (int)(s);*/
	/*mapping(s);*/
	int m=strlen(s);
	while(m>0){
		s[m-1]=s[m-1]+3;
		m--;	
	}
	// s = s+3;
	printf("output is = %s\n",s);
	return 0;
}
/*void mapping(char x[])
{
	while(x!="\n")
	{
		printf("hello\n");
		if((int)(x)<85 && (int)(x) > 65)
		{
			printf("hello2\n");
			(x) = (int)(x)+5;
		}
		else if((int)(x)>= 85)
		{
			printf("hello3\n");
			(x) = (int)-20;
		}
		else if ((int)(x)<117 && (int)(x)>91)
		{
			printf("hello4\n");
			(x) = (int)(x)+5;
		}
		else if((int)(x)>=117) 
		{
			printf("hello5\n");
			(x) = (int)(x)-20;
		}
	}
}*/