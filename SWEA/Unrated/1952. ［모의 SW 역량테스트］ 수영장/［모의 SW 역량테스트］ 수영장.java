import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int[] costs;
	static int[] schedules;
	static int[] minSum;
	static int[] durations = { 12, 3, 1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			costs = new int[4];
			schedules = new int[12];
			minSum = new int[13];
			Arrays.fill(minSum, Integer.MAX_VALUE);

			for (int i = 3; i >= 0; i--) {
				costs[i] = Integer.parseInt(st.nextToken());
			}

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 12; i++) {
				schedules[i] = Integer.parseInt(st.nextToken());
			}

			dfs(0, 0);

			System.out.printf("#%d %d\n", tc, minSum[12]);
		}
	}

	static void dfs(int month, int sum) {
		// month가 12 넘으면 minSum 갱신
		if (month >= 12) {
			minSum[12] = Math.min(sum, minSum[12]);
			return;
		}

		// 4가지 요금으로 백트래킹
		for (int i = 0; i < 4; i++) {
			int nextMonth = month + durations[i];
			int nextCost = nextCost(month, i);
			if (nextMonth <= 12) { // 1년 넘어가지 않으면
				if (sum + nextCost < minSum[nextMonth]) {
					minSum[nextMonth] = Math.min(minSum[nextMonth], sum + nextCost);
					dfs(nextMonth, sum + nextCost);
				}
			} else {
				dfs(nextMonth, sum + nextCost);
			}
		}
	}

	static int nextCost(int month, int cost) {
		if (cost == 3) {
			return costs[cost] * schedules[month];
		} else {
			return costs[cost];
		}
	}
}