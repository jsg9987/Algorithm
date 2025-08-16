// 5초, 256MB, T = 50, 1 <= D <= 13, 1 <= W <= 20, 약품없이 통과는 0 출력
// 완탐 연산량 8000만, 최소 투입횟수보다 크면 가지치기, dfs 안넣거나 / A / B , 가지치기 필요

// 핵심 아이디어: dfs 내에서 성능 통과 로직
// 19:58 ~ 20:56
// 디버깅해서 찾은 부분: 다음 재귀에서 possible을 체크하기 때문에 idx+1까지는 검사해줘야함. 따라서 row = D일때 체크하고 return하도록 기저조건 <-> 범위벗어나는 조건 순서 바꿈.

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int D;
	static int W;
	static int K;
	static int[][] film;
	static int minResult;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			D = Integer.parseInt(st.nextToken());
			W = Integer.parseInt(st.nextToken());
			K = Integer.parseInt(st.nextToken());
			minResult = Integer.MAX_VALUE;
			film = new int[D][W];

			for (int i = 0; i < D; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < W; j++) {
					film[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			if (isPossible()) {
				minResult = 0;
			} else {
				dfs(0, 0);
			}

			System.out.printf("#%d %d\n", tc, minResult);
		}
	}

	// dfs
	static void dfs(int row, int cnt) { // 인덱스, 포함개수
		// 기저조건: 재귀마다 통과되는지 확인, 통과하면 갱신하고 종료
		if (isPossible()) {
			minResult = Math.min(minResult, cnt);
			return;
		}
		
		// row 벗어나면 return;
		if(row >= D) return;

		// 가지치기
		if(cnt >= minResult) return;

		// A 포함하는 경우
		int[] temp = new int[W];
		for(int i = 0; i < W; i++) {
			temp[i] = film[row][i];
			film[row][i] = 0;
		}
		
		dfs(row+1, cnt+1);
		
		for(int i = 0; i < W; i++) { // 원상복구
			film[row][i] = temp[i];
		}
		
		// B 포함하는 경우
		temp = new int[W];
		for(int i = 0; i < W; i++) {
			temp[i] = film[row][i];
			film[row][i] = 1;
		}
		
		dfs(row+1, cnt+1);
		
		for(int i = 0; i < W; i++) { // 원상복구
			film[row][i] = temp[i];
		}
		
		// 포함하지 않는 경우
		dfs(row+1, cnt);
	}

	// 성능 검사 테스트 함수
	static boolean isPossible() {
		for(int i = 0; i < W; i++) {
			int cnt = 1;
			for(int j = 1; j < D; j++) {
				if(cnt >= K) {
					break;
				}
				if(film[j][i] == film[j-1][i]) {
					cnt++;
				}else {
					cnt = 1;
				}
			}
			if(cnt <= K-1) return false;
		}
		return true;
	}

}
