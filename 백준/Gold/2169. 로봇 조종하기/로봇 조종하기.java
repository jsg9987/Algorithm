import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] graph = new int[N][M];
		int[][] DP = new int[N][M];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < M; j++) {
				int temp = Integer.parseInt(st.nextToken());
				if (i == 0) {
					DP[i][j] = temp;
				}
				graph[i][j] = temp;
			}
		}

		DP[0][0] = graph[0][0];
		for (int j = 1; j < M; j++) {
			DP[0][j] = DP[0][j - 1] + graph[0][j];
		}

		for (int i = 1; i < N; i++) {

			int[] left_to_right = new int[M];
			left_to_right[0] = DP[i - 1][0] + graph[i][0];

			for (int j = 1; j < M; j++) {
				int from_up = DP[i - 1][j] + graph[i][j];
				int from_left = left_to_right[j - 1] + graph[i][j];

				left_to_right[j] = Math.max(from_up, from_left);
			}

			int[] right_to_left = new int[M];
			right_to_left[M - 1] = DP[i - 1][M - 1] + graph[i][M - 1];

			for (int j = M - 2; j >= 0; j--) {
				int from_up = DP[i - 1][j] + graph[i][j];
				int from_right = right_to_left[j + 1] + graph[i][j];

				right_to_left[j] = Math.max(from_up, from_right);
			}

			for (int j = 0; j < M; j++) {
				DP[i][j] = Math.max(left_to_right[j], right_to_left[j]);
			}

		}

		bw.write(String.valueOf(DP[N - 1][M - 1]));
		bw.flush();
		bw.close();
		br.close();
	}
}