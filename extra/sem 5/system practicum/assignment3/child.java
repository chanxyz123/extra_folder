import java.util.*;
/*import package forkJoinDemoAsyncExample;
*/
public class child
{
	public static void main(String[] args) 
	{

    int pid = fork();

	if ( pid == 0 )
	{
		System.out.println( "This is being printed from the child process\n" );
	}
	 else 
	 {
		System.out.printf( "This is being printed in the parent process:\n the process identifier (pid) of the child is %d\n", pid );
	 }
	}
}