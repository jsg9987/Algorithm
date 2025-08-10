import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

// 핵심 아이디어: 2^20 * 20 = 100만 * 20 이내라서 완탐 가능하다고 판단함. 처음에 Map형태로 재료를 검사하면서 DFS로 풀려했는데 실패함.
// 복기
// 1. DFS
// 시간복잡도: O(2^N * N) 공간복잡도 O(N^2 + N + c(N)) => O(N^2) | 충돌 쌍 2 * M을 저장하긴 하지만 입출력이니까 제외
// 재료의 궁합은 양방향이기 때문에 HashMap은 어울리지 않음. -> 인접 리스트나 인접 행렬이 어울린다.
// 모든 경우를 탐색하기 때문에 개수를 칭하는 target은 dfs에 필요 없다.
// 2. Bit Mask
// 
public class Solution {
	static int N, M;
	static boolean[] visited;
	static boolean[][] isConflict;
	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());
			M = Integer.parseInt(st.nextToken());

			isConflict = new boolean[N + 1][N + 1];
			visited = new boolean[N + 1]; // 1~10 방문 체크 1차원배열
			result = 1; // 공집합 미리 카운트

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				isConflict[a][b] = true;
				isConflict[b][a] = true;
			}

			// 첫 번째 재료부터 재료를 추가하는 조합 탐색 시작
			// 1번 부터 N번 재료까지 탐색
//			dfs(1);
			int result = countValidBurgers();

			System.out.printf("#%d %d\n", tc, result);
		}

		br.close();
//		bw.close();
	}

	public static void dfs(int idx) {
		// 모든 재료 탐색했으면 return
		if (idx > N) {
			return;
		}

		// 현재 재료를 포함하는 경우
		// 넣으면 충돌나는지 확인
		boolean canAdd = true;
		for (int i = 1; i < idx; i++) {
			// visited && 충돌 확인
			if (visited[i] && isConflict[i][idx]) {
				canAdd = false;
				break;
			}
		}

		if (canAdd) {
			visited[idx] = true;
			result++;
			dfs(idx + 1);
			visited[idx] = false; // 백트래킹
		}

		// 포함하지 않는 경우
		dfs(idx + 1);
	}

	public static int countValidBurgers() {
		int result = 1;
		
		// 모든 가능한 재료 조합을 비트마스킹으로 순회
		// 1 ~ (1 << N) -1까지 순회해서 공집합 제외 모든 부분집합 탐색
		for(int i = 1; i < (1 <<N); i++) {
			boolean isValid = true;
			
			// i 조합의 j,k 재료가 충돌하는지 확인
			for(int j = 1; j <= N; j++) {
				if((i & (1 << (j-1))) != 0) { // j번 재료가 1인지 확인
					for(int k = j + 1; k <= N; k++) {
						if((i & (1 << (k-1))) != 0) { // k번 재료가 1인지 확인
							// 두 재료 모두 포함되었고, 충돌하면?
							if(isConflict[j][k]) {
								isValid = false;
								break;
							}
						}
					}
				}
				if(!isValid) {
					break;
				}
			}
			if(isValid) result++;
		}
		return result;
	}

}