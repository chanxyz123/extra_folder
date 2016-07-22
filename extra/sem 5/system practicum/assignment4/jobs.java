import java.util.*;

class jobs extends Thread
{
	private Scanner x;
	private int p;
	private String y,yo;
	public void job1() throws Exception
	{
		Thread t1 = new Thread(new Runnable()
		{
			public void run()
			{
				x = new Scanner(System.in);
				yo = x.nextLine();
				String var = "[ ]+";
				String[] token = yo.split(var);
				p = Integer.parseInt(token[0]);
				y = token[1];
				System.out.println("job1 ="+p + " " + y);
			}
		});
		Thread t2 = new Thread(new Runnable()
		{
			public void run()
			{
     			int asci;
     			System.out.print("job2 = ");
     			for(int i=0;i<y.length();i++)
     			{
	     			char ch = y.charAt(i);
	   		 		asci = (int)((int)ch+3);
	    			ch = (char)asci;
	    			System.out.print(ch);
     			}
     			System.out.println();
			}
		});
		Thread t3  = new Thread(new Runnable()
		{
			public void run()
			{
					System.out.print("job3 = ");
					int q=1;
					long temp=0;
					long arr[] = new long[2];
					arr[0] =0;
					arr[1] =1;
					if(p==0 || p==1)
					{
						System.out.println(p);
					}
					else
					{	
						while(q<p)
						{
							temp = arr[0]+arr[1];
							arr[0] = arr[1];
							arr[1] = temp;
							q++;
						}
						System.out.println(temp);
					}
			}
		});
		Thread t4 = new Thread(new Runnable()
		{
			public void run()
			{
				int asci;
				System.out.print("job4 = ");
			    int q=1;
			    long temp=0;
				long arr[] = new long[2];
				arr[0] =0;
				arr[1] =1;
				if(p==0 || p==1)
				{
					System.out.println(p+"  ");
				}
				else
				{	
					while(q<p)
					{
						temp = arr[0]+arr[1];
						arr[0] = arr[1];
						arr[1] = temp;
						q++;
					}
				}
				System.out.print(temp + "  ");
				for(int i=0;i<y.length();i++)
     			{
	     			char ch = y.charAt(i);
	   		 		asci = (int)((int)ch+3);
	    			ch = (char)asci;
	    			System.out.print(ch);
     			}
				System.out.println();
			}
		});
		t1.start();
		t1.join();
		t2.start();
		t2.join();
		t3.start();
		t3.join();
		t4.start();
		t4.join();
	}
}