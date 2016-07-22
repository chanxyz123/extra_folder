/*#include <iostream>
#include <cstdlib>
#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <sys/wait.h>
#include <sys/types.h>
/*#include <sys/time.h>*/
/*#include <sys/resource.h>*/
/*#include <sys/wait.h>*/
/*#define	__WAIT_INT(status)*/
#include "stdio.h"


/*using namespace std;*/


int main(void)
{
	/*__pid_t wait();*/
	/*char *argv[3] = {"Command-line", ".", NULL};*/
	int pid = fork();

	if ( pid == 0 ) {
		printf( "After the fork, the process identifier (pid) "
		        "of the child is %d\n", (int)getpid() );


	} else {
		wait(5);
		printf( "After the fork, the process identifier (pid) "
		        "of the parent is still %d\n - fork() returned %d\n",
		        (int)getpid(), pid );
		
	}


	return 0;
} 