import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int sum = 0;
		
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for(int i = 0; i < 5; i++) {
			int cur = Integer.parseInt(st.nextToken()); 
			sum += cur * cur;
		}
		
		System.out.println(sum % 10);
	}
}