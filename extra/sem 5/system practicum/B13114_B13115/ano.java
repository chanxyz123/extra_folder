import java.util.*;

class ano
{
	private Scanner x;
	private int in;
	public int y;
	private int mat[][] = new int[4000][4000];
	public int size()
	{
		x =new Scanner(System.in);
		y = x.nextInt();
		return y;
	}
	public void get()
	{
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				if((j%2)==0)
				{
					mat[i][j] = 1;
				}
				else
				{
					mat[i][j] = 2;
				}
			}
		}
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				/*System.out.print(mat[i][j]+ " ")*/;
			}
			/*System.out.println();*/
		}
	}
	public void multiplecation(int i)
	{
		in = i;
		Thread t1 = new Thread(new Runnable()
		{
			public void run()
			{
				int fmat[][] = new int[y+1][y+1];
				int z=0;
				for(int j=1;j<=y;j++)
				{
					for(int k=1;k<=y;k++)
					{
						z += mat[in][k]*mat[k][j];
					}
				fmat[in][j] = z;
				z=0;
				}		
			}
		});
		t1.start();
	}
	public void multiplecation1(int i)
	{
		in = i;
				int fmat[][] = new int[y+1][y+1];
				int z=0;
				for(int j=1;j<=y;j++)
				{
					for(int k=1;k<=y;k++)
					{
						z += mat[in][k]*mat[k][j];
					}
				fmat[in][j] = z;
				z=0;
				}
	}
}
