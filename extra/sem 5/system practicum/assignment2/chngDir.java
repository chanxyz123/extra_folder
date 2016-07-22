
import java.io.File;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author King
 */

//class to change directory
public class chngDir {

    public String chndir(int length, String[] path) {

        switch (length) {//if user only types cd
            case 1:
                System.out.print(System.getProperty("user.dir"));
                break;

            case 2: //if user enters some argument with cd
                boolean result = false;  // Boolean indicating whether directory was set
                File directory;       // Desired current working directory

                directory = new File(path[1]).getAbsoluteFile();//The java.io.File.getAbsoluteFile() method returns the absolute form of this abstract pathname.
                if (directory.exists()) {   //if the directory path exists
                    result = (System.setProperty("user.dir", directory.getAbsolutePath()) != null);
                }
                break;
        }
        //returning the current path
        return System.getProperty("user.dir");

    }

}
