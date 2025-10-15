import java.io.*;
import java.util.*;

/*
 * 
 */

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		boolean winner = false; // false면 상근, true면 창영 win
		
		while(true) {
			if(N > 3) {
				N -= 3;
				winner = !winner;
				
			}else if(N == 2) {
				N -= 1;
				winner = !winner;
			}else if(N == 1 || N == 3) {
				if(winner == false) {
					System.out.println("SK");
				}else {
					System.out.println("CY");
				}
				break;
			}
		}
	}
}