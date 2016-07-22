import java.util.*;

public class help
{
	public void Help(String x)
	{
		readfile yo = new readfile();
		yo.openFile();
		if(x.equals("cd"))
		{
			yo.readFile(1);
		}
		else if(x.equals("clr"))
		{
			yo.readFile(2);
		}
		else if(x.equals("dir"))
		{
			yo.readFile(3);
		}
		else if(x.equals("environ"))
		{
			yo.readFile(4);
		}
		else if(x.equals("echo"))
		{
			yo.readFile(5);
		}
		else if(x.equals("pause"))
		{
			yo.readFile(6);
		}
		else if(x.equals("quit"))
		{
			yo.readFile(7);
		}
		else
		{
			System.out.println("No help topics match.try ' help '");
		}
		yo.closeFile();
	}
}