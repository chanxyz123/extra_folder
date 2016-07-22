import java.util.*;

class prac extends Thread
{
	private static int x,ii;
	private static Thread t1;
	public static void main(String[] args) 
	{
		
			System.out.println("Number of students " );
			get(10);	
	}

	public static void get( int in)
	{
		ii =in;
		t1 = new Thread(new Runnable()
			{
				public void run()
				{
					for(int i=0;i<=ii;i++)
					{
						x = i; 
						System.out.println(x);
					}
				}
			});
						t1.start();
	}
}