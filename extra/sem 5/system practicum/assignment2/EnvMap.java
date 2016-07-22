
import java.util.Map;
//class to get current environment variables
public class EnvMap {
    public void envmap (){
        Map<String, String> env = System.getenv();	//using map data structure key-value pair
        for (String envName : env.keySet()) {	
        if(envName.equals("SHELL"))
        {
        	System.out.format("%s= %s%n",
                              envName,
                              System.getProperty("user.dir"));

        }	
        else
            {System.out.format("%s=%s%n",
                                          envName,
                                          env.get(envName));}
        }
    }
}