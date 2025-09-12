import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int N = Integer.parseInt(st.nextToken()); // 집하장 개수(정점) 1<= N <= 200
		int M = Integer.parseInt(st.nextToken()); // 집하장간 경로 개수(간선) 1 <= M <= 10000
		int[][] graph = new int[N + 1][N + 1];
		int[][] pathTable = new int[N + 1][N + 1];
		int[][] wayPoints = new int[N + 1][N + 1];
		int INF = 1_000_000_000;

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());

			if (a != b) {
				graph[a][b] = time;
				graph[b][a] = time;
			}
		}

		// graph 초기화
		for (int i = 1; i < N + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				if (i != j && graph[i][j] == 0) {
					graph[i][j] = INF;
				}
			}
		}

//		for(int[] e : graph) {
//			System.out.println(Arrays.toString(e));
//		}

		// pathTable 초기화
		for (int i = 1; i < N + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				if (graph[i][j] > 0 && graph[i][j] != INF) {
					pathTable[i][j] = j;
				}
			}
		}

//		for (int i = 0; i < N + 1; i++) {
//			System.out.println(Arrays.toString(pathTable[i]));
//		}
//		System.out.println();

		for (int k = 1; k < N + 1; k++) {
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j < N + 1; j++) {
					if (i == j) {
						continue;
					}
					if (graph[i][j] > graph[i][k] + graph[k][j]) {
						pathTable[i][j] = pathTable[i][k];
						graph[i][j] = graph[i][k] + graph[k][j];
					}
				}
			}
		}

		for (int i = 1; i < N + 1; i++) {
			for (int j = 1; j < N + 1; j++) {
				if (pathTable[i][j] == 0) {
					sb.append("- ");
				} else {
					sb.append(pathTable[i][j]).append(" ");
				}
			}
			sb.append("\n");
		}

		System.out.println(sb.toString());
	}
}