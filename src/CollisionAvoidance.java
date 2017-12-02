import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class CollisionAvoidance {
	
		public static void main(String args[]) throws IOException {
			
		    try {
		        File input = new File("CollisionLatest.aadl");
		        File output = new File("output.txt");
		        File temp = new File("CollisionLatest.txt");
		        Scanner sc = new Scanner(input);
		        PrintWriter printer = new PrintWriter(output);
		        PrintWriter printer1 = new PrintWriter(temp);
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


