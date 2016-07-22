import java.util.*;

class mat
{
	private Scanner x;
	private int y;
	private int mat1[][] = new int[4000][4000];
	private int mat2[][] = new int[4000][4000];
	public void size()
	{
		x =new Scanner(System.in);
		y = x.nextInt();
	}
	public void get()
	{
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				if((j%2)==0)
				{
					mat1[i][j] = 1;
					mat2[i][j] = 1;
				}
				else
				{
					mat1[i][j] = 2;
					mat2[i][j] = 2;
				}
			}
		}
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				System.out.print("-->"+mat1[i][j]+ "    ");
			}
			System.out.println();
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
					z += mat1[i][k]*mat2[k][j];
				}
				fmat[i][j] = z;
				z=0;
			}

		}
		for(int i=1;i<=y;i++)
		{
			for(int j=1;j<=y;j++)
			{
				System.out.print("-->"+fmat[i][j]+ "   ");
			}
			System.out.println();
		}
	}
}
