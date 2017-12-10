import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class CollisionAvoidance {
	
		public static void main(String args[]) throws IOException {
			Scanner keyboard = new Scanner(System.in);
			System.out.println("Enter the name of the file");
	        String name = keyboard.next();
	        String filename;
			//System.out.println(name);
		    try {
		        File input = new File(name);
		        String separator = System.getProperty("file.separator");
		        int lastSeparatorIndex = name.lastIndexOf(separator);
		        int extensionIndex = name.lastIndexOf(".");
		        filename = name.substring(lastSeparatorIndex + 1);
		        name=filename.substring(0, extensionIndex);
		        File output = new File(name+".py");
		        File temp = new File(name+".txt");
		        Scanner sc = new Scanner(input);
		        PrintWriter printer = new PrintWriter(output);
		        PrintWriter printer1 = new PrintWriter(temp);
		        String variable = "x";
		        while(sc.hasNextLine()) {
		            String s = sc.nextLine();
		            String search = "data port Base_Types";
		            String search2 = "const";
		            String search3 = "eq";
		           
		            if ( s.toLowerCase().indexOf(search.toLowerCase()) != -1 || s.toLowerCase().indexOf(search2.toLowerCase()) != -1 || s.toLowerCase().indexOf(search3.toLowerCase()) != -1 ) {
		            	String newString = s.replaceAll("^\\s+", "").replace("eq", "agree^Eq").replace("const", "agree^const").replace(": ", "@").replace(" ", "_").replace("::", " # ");
		            	   s = newString;
		            }
		            
		            String search4 = "assume";
		            String search5 = "guarantee";
		            if ( s.toLowerCase().indexOf(search4.toLowerCase()) != -1 || s.toLowerCase().indexOf(search5.toLowerCase()) != -1 ) {
		            	 printer1.write(s);  
		            	 s = "";
		            	 System.out.println(s);
		            }
		            
		            String search6="if";
		            String search7="then";
		            String search8="assign";
		            
		            if ( s.toLowerCase().indexOf(search6.toLowerCase()) != -1 &&  s.toLowerCase().indexOf(search7.toLowerCase()) != -1 && s.toLowerCase().indexOf(search8.toLowerCase()) != -1) {
		            	variable = s.substring(s.indexOf(search8) + 6, s.indexOf('='));
		         
		            	String s2  = s.substring(s.indexOf("then") + 4);
		            	s = s.substring(s.indexOf(search6));
		            	s = s.replace("then", ": \n"+  variable + "=");
		            } 
		            String search10="else if";
		            if ( s.toLowerCase().indexOf(search10.toLowerCase()) != -1 ) {
		            	s=s.replace("else if", "elif");
		             	String s3 = s.substring(s.indexOf("then") + 4);
		            	s = s.replace("then", ": \n" + variable + "=");
		            	
		            } 
		            
		            
		            s= s + "\r\n";
		            System.out.println(s);
		            printer.write(s);	        
	                
		        }
		        printer.close();
		        printer1.close();
		        
		    }
		    catch(FileNotFoundException e) {
		        System.err.println("File not found. Please scan in new file.");
		    }
		}
}


