
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
public class fillings {

    public void show() {
        chngDir CD2 = new chngDir();
        String[] pseudo = {"1"};
        File f = new File(CD2.chndir(3,pseudo));
        File[] list = f.listFiles();
        for (File X : list) {
            System.out.println(X+"\n"); 
        }
    }
}
