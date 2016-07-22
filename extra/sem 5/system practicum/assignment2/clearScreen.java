/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
import java.util.*;
import java.io.*;
/**
 *
 * @author King
 */
//class to clear screen by looping '\n' for 1000
public class clearScreen {
    public void loopClear() throws IOException
     {
     	/*int count = 0; 
        int i =0;
        for(;i<1000;i++){
 
System.out.print(String.format("\033[%dA",count)); // Move up
System.out.print("\033[2K"); // Erase line content 
  } */
   final String ANSI_CLS = "\u001b[2J";
        final String ANSI_HOME = "\u001b[H";
        System.out.print(ANSI_CLS + ANSI_HOME);
        System.out.flush();
}
}
