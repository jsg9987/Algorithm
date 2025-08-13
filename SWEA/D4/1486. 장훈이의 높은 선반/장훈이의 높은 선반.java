import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N;
	static int B;
	static int minMax;
	static int[] arr;
	static boolean[] isSelected;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			B = Integer.parseInt(st.nextToken());
			minMax = Integer.MAX_VALUE;
			arr = new int[N];
			isSelected = new boolean[N];

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}

			dfs(0); // 부분집합

			System.out.printf("#%d %d\n", tc, minMax - B);
		}
	}

	static void dfs(int cnt) {
		// 기저 조건: 선택을 마쳤을 때
		if (cnt == N) {
			int sum = 0;
			for (int i = 0; i < N; i++) {
				if (isSelected[i])
					sum += arr[i];
			}
			if (sum >= B && sum < minMax) {
				minMax = sum;
			}
			return;
		}

		// 부분 조합 로직
		isSelected[cnt] = true;
		dfs(cnt + 1);
		isSelected[cnt] = false;
		dfs(cnt + 1);
	}
}