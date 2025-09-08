import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int[] cost;
	static int[] usePlan;
	static int[] DP;
	static int[] periods = { 1, 1, 3, 12 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			cost = new int[4];
			usePlan = new int[13];
			DP = new int[13];
			DP[0] = 0;
			usePlan[0] = 0;

			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for (int i = 0; i < 4; i++) {
				cost[i] = Integer.parseInt(st.nextToken());
			}

			st = new StringTokenizer(br.readLine().trim());
			for(int i = 1; i < 13; i++) {
				usePlan[i] = Integer.parseInt(st.nextToken());
			}
			
			for (int i = 1; i < 13; i++) {
				int localMin = Integer.MAX_VALUE;
				for (int j = 0; j < 4; j++) {
					if (j == 0) {
						localMin = Math.min(localMin, DP[i - 1] + usePlan[i] * cost[j]);
					} else {
						localMin = Math.min(localMin,
								(i - periods[j] >= 0) ? DP[i - periods[j]] + cost[j] : DP[0] + cost[j]);
					}
				}
				DP[i] = localMin;
			}
			
			System.out.printf("#%d %d\n", tc, DP[12]);

		}
	}
}