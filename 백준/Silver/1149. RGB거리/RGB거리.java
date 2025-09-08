import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

/*
 * 
 * 시간복잡도: O(N) 공간복잡도: O(3N) => O(N)
 */
public class Main {
	static int[][] DP;
	static int[][] housePaintCost;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		housePaintCost = new int[N + 1][3];
		DP = new int[N + 1][3];
		for (int i = 1; i < N + 1; i++) {
			Arrays.fill(DP[i], Integer.MAX_VALUE);
		}
		DP[0][0] = DP[0][1] = DP[0][2] = 0;

		for (int i = 1; i < N + 1; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < 3; j++) {
				housePaintCost[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		for(int i = 1; i < N+1; i++) {
			int localMin = Integer.MAX_VALUE;
			
			DP[i][0] = Math.min(DP[i-1][1] + housePaintCost[i][0], DP[i-1][2] + housePaintCost[i][0]);
			DP[i][1] = Math.min(DP[i-1][2] + housePaintCost[i][1], DP[i-1][0] + housePaintCost[i][1]);
			DP[i][2] = Math.min(DP[i-1][0] + housePaintCost[i][2], DP[i-1][1] + housePaintCost[i][2]);
		}
		
		int result = Integer.MAX_VALUE;
		for(int i = 0; i < 3; i++) {
			result = Math.min(result, DP[N][i]);
		}
		
		System.out.println(result);
	}
}