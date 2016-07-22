import java.util.*;
/*package demo1;*/
class runner extends Thread
{
	private float starttime1;
	private float starttime2;
	private float endtime1;
	private float endtime2;
	private ano m;
	private int x;
	private matrix mat;
	private Thread t1;
	public void mat() throws Exception
	{
		m = new ano();
		x = m.size();
		m.get();
		starttime1 = System.nanoTime();
		 t1 = new Thread(new Runnable()
		{
			public void run()
			{
				for(int i = 1;i<=x;i++)
				{
				m.multiplecation(i);
				}
			}
		});
		 for(int i=0;i<x;i++)
		 {
		 	t1.start();
		 }
		endtime1 = System.nanoTime();
		
		mat  = new matrix();
		mat.size(x);
		starttime2 = System.nanoTime();
		mat.multiplecation();
		endtime2 = System.nanoTime();
		float first =(endtime1-starttime1)/1000000000;
		float second = (endtime2-starttime2)/1000000000;
		System.out.println(first + "    " +second );
	}
}