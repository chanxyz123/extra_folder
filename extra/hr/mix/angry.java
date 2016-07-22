import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class angry{

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner x = new  Scanner(System.in);
        int x1 = x.nextInt();
        String var = "[ ]+";
        int x2,x4=0;
        for(int i=0;i<x1;i++)
            {
            Scanner yo = new  Scanner(System.in);
            String y = yo.nextLine();
            String[] temp = y.split(var);
            int x3 = Integer.parseInt(temp[0]);
            x2 = Integer.parseInt(temp[1]);
            String y1 = yo.nextLine();
            String[] temp1 = y1.split(var);
            for(int j=0;j<x3;j++)
                {

                int x5 = Integer.parseInt(temp1[j]); 
                x4 = x4+x5;
            }
            if(x4>=x2)
                {
                System.out.println("NO");
            }
            else
                {
                System.out.println("YES");
            }
        }
    }
}