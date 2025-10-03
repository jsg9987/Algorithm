import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static int[] guiltyScore;
	static int[][] R;
	static int eunjin;
	static int maxNight;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		// 1. 입력 처리
		N = Integer.parseInt(br.readLine().trim());
		guiltyScore = new int[N];
		R = new int[N][N];
		maxNight = 0;

		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for (int i = 0; i < N; i++) {
			guiltyScore[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < N; j++) {
				R[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		eunjin = Integer.parseInt(br.readLine().trim());

		// N이 홀수이면 첫 라운드는 낮으로 시작하여 바로 종료될 수 있으므로,
		// 참가자 수(N)와 밤 횟수(0)만 인자로 넘깁니다. (deadCitizen은 생략)
		dfs(N, 0);

		System.out.println(maxNight);
	}

    /**
     * @param survivor 현재 생존자 수
     * @param nightCnt 현재까지 진행된 밤의 횟수
     */
	private static void dfs(int survivor, int nightCnt) {
		
		// 1. 기저 조건: 마피아 승리 (은진만 남음)
		// 생존자가 1명만 남았을 때 (마피아인 은진) 게임 종료
		if (survivor == 1) {
			maxNight = Math.max(maxNight, nightCnt);
			return;
		}

		// 2. 유도 단계
		if (survivor % 2 == 0) { // 밤 (짝수 명) - 마피아 턴
			
			for (int i = 0; i < N; i++) {
				// 이미 죽은 사람(-1)이거나 마피아인 은진은 건너뛴다.
				if (guiltyScore[i] == -1 || i == eunjin)
					continue; 

				// --- 마피아 행동 (Kill & Update Score) ---
				int temp = guiltyScore[i];
				guiltyScore[i] = -1; // i번 시민을 죽임
				
				// 유죄 지수 업데이트
				for (int j = 0; j < N; j++) {
					// i번 자신, 이미 죽은 사람은 제외하고 업데이트
					if (guiltyScore[j] != -1 && i != j) { 
						guiltyScore[j] += R[i][j];
					}
				}
				
				// 다음 라운드(낮)로 재귀 호출 (밤 횟수 증가)
				dfs(survivor - 1, nightCnt + 1); 
				
				// --- 백트래킹 (상태 복원) ---
				for (int j = 0; j < N; j++) {
					// i번 자신, 이미 죽은 사람은 제외하고 복원
					if (guiltyScore[j] != -1 && i != j) { 
						guiltyScore[j] -= R[i][j];
					}
				}
				guiltyScore[i] = temp;
			}
			
		} else { // 낮 (홀수 명) - 시민 턴
			
			// --- 유죄 지수 최대값인 사람 찾기 ---
			int killIdx = -1;
			int maxValue = -1; 
			
			for (int i = 0; i < N; i++) {
				if (guiltyScore[i] == -1) continue;

				// 유죄 지수가 더 크거나, 같을 때 번호가 작은 사람(먼저 탐색된 i)이 선택된다.
				if (guiltyScore[i] > maxValue) {
					killIdx = i;
					maxValue = guiltyScore[i];
				}
			}
			
			// 3. 기저 조건: 마피아 패배 (낮에 은진이 죽는 경우)
			if (killIdx == eunjin) {
				maxNight = Math.max(maxNight, nightCnt); // 죽기 직전의 nightCnt 갱신
				return;
			}

			// --- 시민 행동 (Kill & DFS Call) ---
			
			// 유죄 지수 가장 높은 시민 제거
			int temp = guiltyScore[killIdx];
			guiltyScore[killIdx] = -1; 

			// 다음 라운드(밤)로 재귀 호출 (밤 횟수 유지)
			dfs(survivor - 1, nightCnt); 

			// --- 백트래킹 (상태 복원) ---
			guiltyScore[killIdx] = temp;
		}
	}
}