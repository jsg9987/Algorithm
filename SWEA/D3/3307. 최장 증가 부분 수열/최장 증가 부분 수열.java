import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			int N = Integer.parseInt(br.readLine().trim());
			int[] arr = new int[N + 1];
			int[] DP = new int[N + 1];

			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for (int i = 1; i < N + 1; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}

			int max = 0;
			for (int i = 1; i < N + 1; i++) {
				DP[i] = 1;
				for (int j = 1; j < i; j++) {
					if (arr[j] < arr[i]) {
						DP[i] = Math.max(DP[i], DP[j] + 1);
					}
				}
				
				max = Math.max(max, DP[i]);
			}
			
			System.out.printf("#%d %d\n", tc , max);
			
		}
	}
}