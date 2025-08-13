import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

// 핵심 아이디어: 3군데로 나눠서 sum
// 시간복잡도: O(N^2) 공간복잡도: O(N^2)
public class Solution {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < T + 1; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[][] arr = new int[N][N];
			int mid = N / 2;
			int sum = 0;
//			boolean[][] visited = new boolean[N][N]; // 디버깅

			for (int i = 0; i < N; i++) {
				String input = br.readLine();
				for (int j = 0; j < N; j++) {
					arr[i][j] = input.charAt(j) - '0';
				}
			}

			// 위에 절반
			for (int i = 0; i < N / 2; i++) {
				for (int j = mid - i; j < N + i - mid; j++) {
					sum += arr[i][j];
				}
			}
			
			// 가운데 줄
			for (int i : arr[mid]) {
				sum += i;
			}
			
			// 아래 절반
			for (int i = mid + 1; i < N; i++) {
				for (int j = i - mid; j < N - i + mid; j++) {
					sum += arr[i][j];
				}
			}

			System.out.printf("#%d %d\n", tc, sum); // printf 항상 개행 주의
		}
		br.close();
	}
}