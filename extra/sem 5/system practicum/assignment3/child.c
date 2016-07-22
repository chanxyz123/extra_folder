
#define	__WAIT_INT(status)
#include "stdio.h"



void p_child(int x)
{
		int pid = fork();

	if ( pid == 0 ) {
		
		/*sleep(3+x);
		x=0;*/
		printf( "After the fork, the process identifier (pid) "
		        "of the child is %d\n", (int)getpid() );

	} else {
/*		wait(10000);*/
		sleep(x);
		printf( "After the fork, the process identifier (pid) "
		        "of the parent is still %d\n - fork() returned %d\n",
		        (int)getpid(), pid );
		
	}
}
int main(void)
{
	int x,y=0;
	char ch;
	printf("Press Number \n");
	printf("1.child terminates before its parent.\n");
	printf("2.parent terminates before child.\n");
	printf("3.function is used to make parent wait.\n");
	scanf("%d",&x);
	if(x==1)
	{
		p_child(2);
	}
	else if(x==2)
	{
		p_child(0);
	}
	else if(x==3)
	{
		printf("wait()\n");
	}
	return 0;
} 