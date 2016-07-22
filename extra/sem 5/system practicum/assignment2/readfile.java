import java.io.*;
import java.util.*;
import java.lang.*;
/*import java.io.IOException;
import java.io.FileReader;
import java.util.Scanner;*/

public class readfile
{
	private Scanner x;

	public  void openFile()
	{
		//File temp = new File("sample.txt");
		try {
			x = new Scanner (new FileReader("help.txt"));
		}
		catch(Exception e)
		{
			System.out.println("File not found");
		}
	}

	public void readFile(int s) 
	{
		try 
		{
			int y=1;
			//Scanner x = new Scanner (new FileReader("sample.txt"));
			while(x.hasNextLine())
			{
				String l = x.nextLine();
				if(s == y)
				{
					
					System.out.print(l);
					//System.out.println("cjn");
					break;
				}
				y++;
				//System.out.printf("%s %s",a,b);
			}
		}
		catch (Exception e) {
			System.out.println("Error while reading file " + e);
		}
	}

	public void closeFile()
	{
		try {
				x.close();
			}
		catch (Exception e) {
			System.out.println("Error while closing " + e);
		}
	}

	

}