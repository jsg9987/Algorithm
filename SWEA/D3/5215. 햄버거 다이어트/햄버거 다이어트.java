import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int i = 0; i < T; i++) {
			List<int[]> li = new ArrayList<>();
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int l = Integer.parseInt(st.nextToken());
			int[][] dp = new int[n + 1][l + 1];

			for (int j = 0; j < n; j++) {
				st = new StringTokenizer(br.readLine());
				int len = st.countTokens();
				int[] temp = new int[len];
				for (int k = 0; k < len; k++) {
					temp[k] = Integer.parseInt(st.nextToken());
				}
				li.add(temp);
			}

			Collections.sort(li, Comparator.comparingInt(o -> o[1]));

			for (int k = 1; k < n + 1; k++) {
				int[] temp = li.get(k-1);
				int point = temp[0];
				int kcal = temp[1];
				for (int col = 0; col < l + 1; col++) {
					if (col >= kcal) {
						dp[k][col] = Math.max(dp[k - 1][col - kcal] + point, dp[k - 1][col]);
					} else {
						dp[k][col] = dp[k - 1][col];
					}
				}
			}

			System.out.printf("#%d %d", i+1, dp[n][l]);
            System.out.println();
		}
	}
}