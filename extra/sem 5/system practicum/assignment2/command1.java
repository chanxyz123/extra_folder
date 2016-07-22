/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author King
 */
import java.util.*;
import java.io.*;
public class command1{

	public void start(String[] x) throws IOException
	{
		int len = x.length;
		//block to call change directory class
		if(x[0].equals("cd"))
		{
			if(len <= 2)
			{
                chngDir cd1 = new chngDir();
                cd1.chndir(len,x);
			}
			else 
                System.out.println("too many arguments\n");

		}
		//block to call clear screen class
		else if(x[0].equals("clr"))
		{
			if(len > 1)
                System.out.print("too many arguments\n");
			else
			{
                clearScreen CS1 = new clearScreen();
                CS1.loopClear();
			}
		}
		//block to call directory class
		else if(x[0].equals("dir"))
		{
                        fillings F1 = new fillings();
                        F1.show();
		}
		//block to call environment class
		else if(x[0].equals("environ"))
		{
			if(len > 1)
                            System.out.println("too many arguments\n");
			else
			{
				EnvMap ev = new EnvMap();
				ev.envmap();
			}
		}
		//block to call echo class
		else if(x[0].equals("echo"))
		{
			if(len >= 2)
			{
				for(int i=1;i<len;i++)
				{
					System.out.printf(x[i]);
					System.out.printf(" ");
				}
				System.out.println("\n");
			}
			else 
                            System.out.println("Syntex error!\n");
		}
		//block to pause shell
		else if(x[0].equals("pause"))
		{
			if(len == 1)
			{
				System.out.println("press Enter key to continue.........");
				String st;
				Scanner scc;
				String stt;
				do
				{
					scc = new Scanner (System.in);
					stt = scc.nextLine();
				}while(stt.contains("\\n"));
			}
			else
                            System.out.println("too many arguments\n");
		}
		//block to call help class
		else if(x[0].equals("help"))
		{
			if(len <= 2)
			{
				if(len == 1)
				{
					Scanner sc = new Scanner (new FileReader ("help.txt"));
					while(sc.hasNextLine())
					{
						String str = sc.nextLine();
						System.out.println(str);
					} 
					System.out.println("\n");
				}
				else
				{
					help yoo = new help();
					yoo.Help(x[1]);
					System.out.println("\n");
				}

			}
			else
                            System.out.println("error !\n");
		}
		//if command is not defined
		else 
			System.out.println("Command is not recognised as an internal command");
			System.out.println("\n");
	}

}
