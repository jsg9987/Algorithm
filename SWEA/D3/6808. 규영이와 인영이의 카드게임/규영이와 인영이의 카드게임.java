import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.util.stream.Collectors;

public class Solution {
	static int allSum;
	static int winCnt;
	static int loseCnt;
	static int[] inyung = null;
	static int[] gyung = null;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		// 게임 진행
		for (int tc = 1; tc < T + 1; tc++) {
			gyung = new int[9];
			inyung = new int[9];
			winCnt = 0;
			loseCnt = 0;
			allSum = 0;
			int[] all = new int[18];
			for (int i = 1; i < 19; i++) {
				all[i - 1] = i;
				allSum += i;
			}

			// 배열 초기화
			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 9; i++) {
				gyung[i] = Integer.parseInt(st.nextToken());
				all[gyung[i] - 1] = 0;
				allSum += gyung[i];
			}

			int idx = 0;
			for (int i = 0; i < 18; i++) {
				if (all[i] != 0) {
					inyung[idx] = all[i];
					idx++;
				}
			}

//			System.out.println(Arrays.toString(gyung));
//			System.out.println(Arrays.toString(inyung));

			dfs(0, 0, 0, new boolean[9]);
			System.out.printf("#%d %d %d", tc, winCnt, loseCnt);
			System.out.println();
		}

	}

	static void dfs(int idx, int gyuSum, int inSum, boolean[] visited) { // 규영 idx

		// 종료 조건
		if (idx == 9) {
			if (gyuSum > inSum) {// 승리
				winCnt += 1;
			} else if (gyuSum < inSum) { // 패배
				loseCnt += 1;
			}
			return;
		}

		// 백트래킹을 하면서 결과 찾기
		for (int i = 0; i < 9; i++) {
			// 현재 원소를 골라서 분기 진행
			if (!visited[i]) {
				visited[i] = true;
				// 승패 조건 설정
				if (gyung[idx] > inyung[i]) {
					dfs(idx + 1, gyuSum + inyung[i] + gyung[idx], inSum, visited);
				} else if (gyung[idx] < inyung[i]) {
					dfs(idx + 1, gyuSum, inSum + inyung[i] + gyung[idx], visited);
				}
				visited[i] = false;
			}
		}
	}
}