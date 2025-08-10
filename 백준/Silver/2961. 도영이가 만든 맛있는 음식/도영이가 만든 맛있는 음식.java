import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	static long minResult = Long.MAX_VALUE;
	static int N;
	static long[] sin;
	static long[] sseun;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		StringTokenizer st = null;
		sin = new long[N];
		sseun = new long[N];

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine());
			sin[i] = Long.parseLong(st.nextToken());
			sseun[i] = Long.parseLong(st.nextToken());
		}

		for (int i = 1; i < N + 1; i++) {
			dfs(0, 0, i, 0, 0);
		}

		System.out.println(minResult);
	}

	public static void dfs(int idx, int nowCnt, int target, long sinSum, long sseunSum) {
		// 기저 조건: 목표 개수만큼 골랐을 때
		if (nowCnt == target) {
			minResult = Math.min(Math.abs(sinSum - sseunSum), minResult);
			return;
		}
		
		if(nowCnt > target) {
			return;
		}

		// idx가 끝났을 때
		if (idx == N) {
			return;
		}

		// 골랐을 때
		if (nowCnt == 0) {
			dfs(idx + 1, nowCnt + 1, target, sin[idx], sseunSum + sseun[idx]);
		} else {
			dfs(idx + 1, nowCnt + 1, target, sinSum * sin[idx], sseunSum + sseun[idx]);
		}
		// 안 골랐을 때
		dfs(idx + 1, nowCnt, target, sinSum, sseunSum);

	}

}