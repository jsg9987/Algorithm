// 16:13 ~ 17:35
// 5초, 256MB, tc: 15, 2<=N<=500, 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N, M;
	static boolean[][] adj;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			N = Integer.parseInt(br.readLine().trim());
			M = Integer.parseInt(br.readLine().trim());

			adj = new boolean[N + 1][N + 1];

			for (int i = 0; i < M; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine().trim());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				adj[a][b] = true;
			}

			// 플로이드 워셜
			for (int k = 1; k < N + 1; k++) {
				for (int i = 1; i < N + 1; i++) {
					if (adj[i][k]) {
						for (int j = 1; j < N + 1; j++) {
							if (adj[k][j])
								adj[i][j] = true;
						}
					}
				}
			}

			int result = 0;
			for (int i = 1; i < N + 1; i++) {
				int cnt = 0;
				for (int j = 1; j < N + 1; j++) {
					if (adj[i][j] || adj[j][i])
						cnt++;
				}
				if(cnt == N-1) result++;
			}
			
			System.out.printf("#%d %d\n", tc, result);
		}
	}
}