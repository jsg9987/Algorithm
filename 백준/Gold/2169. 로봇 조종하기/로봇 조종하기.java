import java.io.*;
import java.util.*;

/*
 * 아이디어: BFS와 DP 중 고민함. DP 규칙을 찾으려 했으나 아무리 해도 최소 부분 문제라고 판단되지 않아 BFS 시간복잡도를 계산하고 진행했음.
 * 하지만 BFS를 구현하는 도중 3차원 방문처리를 하려했으나 루트가 다르나 같은 지점으로 들어오는 모든 경우를 중복처리하면 안됐었음.
 * 따라서 시간복잡도가 O(NM)이 아니라 O(3^k)였다. k는 깊어지는 범위 -> 최대 10000임.
 * DP로 풀어야했다.
 * 
 * 복기
 * 위로 가는 것이 불가능하기에 DAG 그래프에 해당함. 따라서 DP로 구현 가능함.
 * 아래, 왼, 오른쪽에서 오는 DP를 3번에 걸쳐 갱신해 최대값을 갱신해야함. 다만 한 배열에서 해버린다면 왼쪽 -> 오른쪽 / 오른쪽 -> 왼쪽의 가는 길의 결과값이 섞여버리기에
 * 2개로 나눠서 처리해야했음.
 * 시간복잡도: O(N*M)
 * 공간복잡도: O(N*M)
 */
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