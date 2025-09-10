import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
	static int INF = 1_000_000;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int N = Integer.parseInt(st.nextToken());
			int[][] graph = new int[N][N];
			int[][] DP = new int[N][N];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					int cur = Integer.parseInt(st.nextToken());
					if (i != j && cur == 0) {
						graph[i][j] = INF;
					} else {
						graph[i][j] = cur;
					}
				}
			}

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					for (int k = 0; k < N; k++) {
						graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
					}
				}
			}

			int minSum = Integer.MAX_VALUE;
			for (int i = 0; i < N; i++) {
				int tempSum = 0;
				for (int j = 0; j < N; j++) {
					tempSum += graph[i][j];
				}
				minSum = Math.min(minSum, tempSum);
			}

			System.out.printf("#%d %d\n", tc, minSum);
		}
	}
}