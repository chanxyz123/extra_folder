import java.util.*;

class matrix
{
	private Scanner x;
	private int y;
	private int mat[][] = new int[4000][4000];
	public void size(int i)
	{
		/*x =new Scanner(System.in);
		y = x.nextInt();*/
		y = i;

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
	public void multiplecation()
	{
		int fmat[][] = new int[y+1][y+1],z=0;
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				for(int k=1;k<=y;k++)
				{
					z += mat[i][k]*mat[k][j];
				}
				fmat[i][j] = z;
				z=0;
			}

		}
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				/*System.out.print(fmat[i][j]+ "    ");*/
			}
			/*System.out.println();*/
		}
	}
}
