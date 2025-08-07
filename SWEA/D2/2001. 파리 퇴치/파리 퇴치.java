import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			int[][] arr = new int[N][N];

			for (int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int newN = N - M + 1;
			int[][] sumArr = new int[newN][newN];
			for (int i = 0; i < N - M + 1; i++) {
				for (int j = 0; j < N - M + 1; j++) {
					for (int k = 0; k < M; k++) {
						for (int l = 0; l < M; l++) {
							sumArr[i][j] += arr[i + k][j + l];
						}
					}
				}
			}
			int maxValue = 0;
			for (int i = 0; i < newN; i++) {
				for (int j = 0; j < newN; j++) {
					maxValue = Math.max(maxValue, sumArr[i][j]);
				}
			}
			System.out.printf("#%d %d",t+1, maxValue);
			System.out.println();
		}
	}
}