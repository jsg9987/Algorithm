import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static boolean[] visited;
	static int maxValue;
	static int minValue;
	static int[] opers;
	static int[] nums;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 1; i < T + 1; i++) {
			N = Integer.parseInt(br.readLine());
			visited = new boolean[4];
			opers = new int[4];
			nums = new int[N];
			maxValue = Integer.MIN_VALUE;
			minValue = Integer.MAX_VALUE;
			StringTokenizer st = new StringTokenizer(br.readLine());

			for (int j = 0; j < 4; j++) {
				opers[j] = Integer.parseInt(st.nextToken());
			}

			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				nums[j] = Integer.parseInt(st.nextToken());
			}

			for (int j = 0; j < 4; j++) {
				if (opers[j] > 0) {
					opers[j]--;
					dfs(1, operate(nums[0], j, nums[1]));
					opers[j]++;
				}
			}

			System.out.printf("#%d %d\n", i, maxValue - minValue);
		}
	}

	static void dfs(int cnt, int result) {
		// 조합 완성 시 최대,최소 비교 (기저)
		if (cnt == N - 1) {
			maxValue = Math.max(maxValue, result);
			minValue = Math.min(minValue, result);
			return;
		}

		for (int i = 0; i < 4; i++) {
			if (opers[i] > 0) {
				opers[i]--;
				dfs(cnt + 1, operate(result, i, nums[cnt + 1]));
				opers[i]++;
			}
		}
	}

	static int operate(int result, int op, int next) {
		switch (op) {
		case 0:
			return result + next;
		case 1:
			return result - next;
		case 2:
			return result * next;
		case 3:
			return result / next;
		}
		return 0;
	}
}