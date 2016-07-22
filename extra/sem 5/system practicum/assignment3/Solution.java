import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
        int x=0;String s1=" ";
            System.out.println("================================");
            for(int i=0;i<3;i++)
            {
                s1=sc.next();
               x=sc.nextInt();
                    System.out.printf("%s \t %03d \n",s1,x);
                //Complete this line
            }
    
            System.out.println("================================");

    }
}