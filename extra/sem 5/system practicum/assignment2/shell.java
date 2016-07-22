import java.util.*;
import java.lang.String;
import java.io.*;

public class shell
{
	public static void main(String[] args) throws IOException
	{
		System.out.println("Welcome to 14-15 shell : \n");
		//declaration and initialisation of variables
		String str = "";
		String check;
		String var = "[ ]+";
		String[] token;

			//block to read input from a file and execute
				if(args.length > 0)
				{
					Scanner file = new Scanner(new FileReader(args[0]));
					while(file.hasNextLine())
					{
						do
						{
							str = file.nextLine();
							token = str.split(var);
							check = token[0].toUpperCase();

							//checking condition to quit
							if(!(check.equals("QUIT")))
							{
								command1 yoo = new command1();
								yoo.start(token);
							}
						}while(!(check.equals("QUIT")));
					}
				}
				else		//if user wants to input by themselves
				{
					do{
						System.out.print(System.getProperty("user.dir") + '$' );		//printing current path
						Scanner x = new Scanner(System.in);
						str = x.nextLine();
						token = str.split(var);
						check = token[0].toUpperCase();
						if(!(check.equals("QUIT")))
						{
							command1 yo = new command1();
							yo.start(token);
						}
					}while(!(check.equals("QUIT")));
				}
	}
}