import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

/*
 * 시간복잡도 O(N), 공간복잡도 O(N)
 */
public class Main {
	static int[] DP;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		DP = new int[N+1];
		Arrays.fill(DP, Integer.MAX_VALUE);
		DP[0] = 0;
		DP[1] = 0;
		
		for(int i = 2; i < N+1; i++) {
			int localMin = Integer.MAX_VALUE;
			
			if(i % 2 == 0) {
				localMin = Math.min(localMin, DP[i/2] + 1);
			}
			if(i % 3 == 0) {
				localMin = Math.min(localMin, DP[i/3] + 1);
			}
			if(i - 1 >= 0) {
				localMin = Math.min(localMin, DP[i-1] + 1);
			}
			
			DP[i] = localMin;
		}
		
		System.out.println(DP[N]);
		
	}
}