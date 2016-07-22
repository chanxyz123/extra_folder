import java.util.*;

public class command{

	public void start(String[] x)
	{
		int len = x.length();
		if(x[0].equals.("CD"))
		{
			if(len <= 2)
			{
				if (len == 1) 
				{
					System.out.println("you are working in home diractory");
				}
				else
				{
					
				}
			}
			else 
			{
				System.out.println("too many arguments")
			}

		}
		else if(x[0].equals("CLR"))
		{
			if(len > 1)
			{
				System,out.println("too many arguments");
			}
			else
			{

			}
		}
		else if(x[0].equals("DIR"))
		{

		}
		else if(x[0].equals("ENVIRON"))
		{
			if(len > 1)
			{
				System.out.println("too many arguments");
			}
			else
			{

			}
		}
		else if(x[0].equals("ECHO"))
		{
			if(len == 2)
			{

			}
			else 
			{
				System.out.println("too many arguments");
			}
		}
		else if(x[0].equals("PAUSE"))
		{
			if(len == 1)
			{

			}
			else
			{
				System.out.println("too many arguments");
			}
		}
		else if(x[0].equals("HELP"))
		{
			if(len <= 2)
			{
				if(len == 1)
				{

				}
				else
				{

				}

			}
			else
			{
				System.out.println("error !");
			}
		}
		else if(x[0].equals("QUIT"))
		{
			if(len == 1)
			{
				
			}
			else
			{
				System.out.println("error !");
			}

		}
		else 
		{
			System.out.println("you are  extra command !");
		}
	}

}

