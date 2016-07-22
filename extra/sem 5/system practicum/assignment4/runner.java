import java.util.*;
/*package demo1;*/
class runner extends Thread
{
	private long starttime1;
	private long starttime2;
	private long endtime1;
	private long endtime2;
	public void mat() throws Exception
	{
		Thread t1 = new Thread(new Runnable()
		{
			public void run()
			{
				matrix m = new matrix();
				m.size();
				m.get();
				starttime1 = System.nanoTime();
				m.multiplecation();
				endtime1 = System.nanoTime();
			}				
		});
	/*	Thread t2 = new Thread(new Runnable()
		{
			public void run()
			{
				matrix m = new matrix();
				m.size();
				m.get();
				starttime2 = System.nanoTime();
				m.multiplecation();
				endtime2 = System.nanoTime();
			}
		});*/
		
				matrix m = new matrix();
				m.size();
				m.get();
				starttime2 = System.nanoTime();
				m.multiplecation();
				endtime2 = System.nanoTime();
		t1.start();
		/*t2.start();*/
		t1.join();
		/*t2.join();*/
		System.out.println(Math.log(endtime1-starttime1) + "    " + Math.log(endtime2-starttime2));
	}
}