import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner x1= new Scanner(System.in);
        Scanner x2= new Scanner(System.in);
        String y1 = x1.nextLine();
        String y2 = x2.nextLine();
        String var = "[ ]+";
        int total;
        String[] token1 = y1.split(var);
        String[] token2 = y2.split(var);
        int z1 = Integer.parseInt(token1[0]);
        int z2 = Integer.parseInt(token2[0]);
        int z3 = Integer.parseInt(token1[1]);
        int z4 = Integer.parseInt(token2[1]);
        int z5 = Integer.parseInt(token1[2]);
        int z6 = Integer.parseInt(token2[2]);
        if(Math.abs(z5-z6)>0)
            {
            total = 10000+500*Math.abs(z3-z4)+15*Math.abs(z1-z2);
            System.out.print(total);
        }
        else if(Math.abs(z3-z4)>0)
            {
            total = 500*Math.abs(z3-z4)+15*Math.abs(z1-z2);
            System.out.print(total);
        }
        else if(Math.abs(z1-z2)>0)
            {
            total = 15*Math.abs(z1-z2);
                System.out.print(total);
        }
        else
            {
      			if()      
             }
    }
}