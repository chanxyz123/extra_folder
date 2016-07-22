import java.io.*;
   import javax.swing.*;
     
    public class SimpleEncryption   
   {
       public static void main (String [] args) throws Exception
      {
         BufferedReader inKb = new BufferedReader (new InputStreamReader (System.in));
       
         for(int i=0; i<10; i++)
         {
            String ans = JOptionPane.showInputDialog ("Hello User, would you like to encrypt or decrypt?");
            ans = ans.toUpperCase();        
            int a = 0;
             
            if (ans.contains("EN")||ans.contains("ENCRYPT"))
            {
               String pass = "";
               pass = JOptionPane.showInputDialog ("Please type your phrase into input:");          
             
               for (int j=0; j<pass.length(); j++)
               {
                  char c = pass.charAt(j);
                  a = (int) c;
                  System.out.print(a);
               }
               break;
            }
             
          
            if (ans.contains("DE")||ans.contains("DECRYPT"))
            {
               String pass = "";
               pass = JOptionPane.showInputDialog ("Please type the encrypted code into input:");          
             
               for (int k=0; k<pass.length(); k++)
               {
                  char c = pass.charAt(k);
                  a = (int)((int)c+3);
                  i = (char) a;
                  System.out.print(i);
               }
               break;
            }
             
            System.out.println("Sorry I don't understand, please retry.");
         }
      }
   }