import java.io.IOException;
import java.io.FileReader;
import java.util.Scanner;

class Rfile
{
	/*public static void main(String[] args) throws IOException
	{
		Scanner cin=new Scanner(new FileReader(args[0]));
		while(cin.hasNextLine())
		{
			String s=cin.nextLine();
			System.out.println(s);
		} 
	}*/
	public static void main(String[] args) throws IOException
	{
		readfile r = new readfile();

		r.openFile();
		r.readFile();
		r.closeFile();
	}
}