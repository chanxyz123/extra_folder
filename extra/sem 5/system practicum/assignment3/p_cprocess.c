#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>

int a[100000];    //prime
int b[100000];  //fib
void makegrandchild(int n, int num, int p);
void makegreatgrandchild(int n, int num, int p , int q);
void makechild(int n,int num);

void makechild(int n,int num)
{
	int i=1,j,k=0,count;
	printf("Child:%d:Prime Numbers upto %d :",n,num);
	while(i<=num)
	{
		count=0;
		for(j=1;j<=i;j++)
		{
			if(i%j==0) //checking whether num is dvisible by j
			count++;
		}
		if(count==2)//if num is divisible by 2 numbers,then it is prime
		{
			printf("%d ",i);
			//printf("Child:%d:Prime Numbers upto %d :%d\n",n,num,i);
			a[k]=i;
			k++;
		} 
		
		i++;

	}
	printf("\n");
	int g1,g2;			
	if (n==1)
	{
		g1=1;
		g2=2;
	}
	else
	{
		g1=3;
		g2=4;
	}
	int pid_grandchild=(int)fork();
		if(pid_grandchild==0) 
		{
			makegrandchild(g1, num,k);
			
		}
		else
		{	
			int pid_grandchild1=(int)fork();

			if (pid_grandchild1==0)
			{
				makegrandchild(g2, num,k);
			}
			/*else
			{
				int status;
				while(&status)
					{wait;}

			}	*/
		}
}


void makegrandchild(int n,int num, int p)
{
	int c,next,first=0,second=1;
  int k=0;
  printf("GrandChild:%d:Fibonacci numbers upto %d :",n,num);
   for ( c = 0 ; c <num ; c++ )
   {
      if ( c <= 1 )
         next = c;
      else
      {
         next = first + second;
         first = second;
         second = next;
      }
      b[k]=next;
      k++;
   }
   int i, f=0;
   
	  for( i=0;i<k;i++)
	  {
	    printf("%d ",b[i]);
	    //printf("GrandChild:%d:Fibonacci numbers upto %d :%d\n",n,num,b[i]);

	  }
	printf("\n");
	int g1,g2;
	if (n==1)
	{
		g1=1;
		g2=2;
	}
	else if(n==2)
	{
		g1=3;
		g2=4;
	}
	else if (n==3)
	{
		g1=5;
		g2=6;
	}
	else if (n==4)
	{
		g1=7;
		g2=8;
	}
	int pid_greatgrandchild=(int)fork();
		if(pid_greatgrandchild==0) 
		{	
			sleep(5);
			makegreatgrandchild(g1, num, p,k);
			
		}
		else
		{	
			int pid_greatgrandchild1=(int)fork();

			if (pid_greatgrandchild1==0)
			{
				sleep(5);
				makegreatgrandchild(g2, num,p ,k);

			}
			/*else
			{
				int status;
				while(&status)
					{wait;}

			}*/
				
		}
}


void makegreatgrandchild(int n,int num, int p ,int q)
{	

	int i = 0, j = 0;
	printf("GreatGrandChild:%d:Intersection numbers upto %d :",n,num);	
  while (i < p && j < q)
  {
    if (a[i] < b[j])
      i++;
    else if (b[j] < a[i])
      j++;
    else /* if arr1[i] == arr2[j] */
    {
      // printf("GreatGrandChild:%d:Intersection numbers upto %d :%d\n",n,num,b[j++]);	
       printf(" %d ", b[j++]);
      i++;
    }
  }
  printf("\n");
   // int i;
   
	  // for( i=0;i<=n;i++)
	  // {
	  //   printf("%d ",b[i]);
	  //   printf("GrandChild:%d:Fibonacci numbers upto %d :%d\n",n,num,b[i]);

	  // }
	// printf("\n\n");
	
}

int main(int argc, char* argv[])
{
	int num=0,status;
	int maxInt=atoi(argv[1]);
	printf("the parent id is %d \n",(int)getpid());
	int pid_child1=(int)fork();
	
	
	if(pid_child1==0) 
	{
		makechild(1, maxInt);
		
	}
	else
	{	
		int pid_child2=(int)fork();

		if (pid_child2==0)
		{
			makechild(2, maxInt);
		}
		/*else
			{
				int status;
				while(&status)
					{wait;}

			}	*/
	}
			
}