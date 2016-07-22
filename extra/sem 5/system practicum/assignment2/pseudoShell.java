import java.io.File;
import java.util.*;
public class pseudoShell
{
        @SuppressWarnings("null")
	public static void main(String[] args) 
	{
		String check;
			do{
                            System.out.println(System.getProperty("user.dir"));
                            
                            //asking for input string from user
				Scanner x = new Scanner(System.in);
				String str = x.nextLine();
				
                            //parsing commands from the string 
                                String var = "[ ]+";
				String[] token = str.split(var);
				check = token[0].toUpperCase();
                                
                            //if they wants to exit 
                                if(check.equals("EXIT"))
                                {
                                    System.out.println("Exiting.......");
                                    break;
                                }

                            //the other code
                                command C1 = new command();
                                C1.start(token);
                                

			}while(true);
	}
}