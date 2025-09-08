import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		int result = 0;
		for(int i = 1; i < N+1; i++) {
			String num = String.valueOf(i);
			int temp = i;
			for(int j = 0; j < num.length(); j++) {
				temp += num.charAt(j) - '0';
			}
			
			if(temp == N) {
				result = i;
				break;
			}
		}
		
		System.out.println(result);
	}
}