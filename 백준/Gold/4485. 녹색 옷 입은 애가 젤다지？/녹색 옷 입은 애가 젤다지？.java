
// 20:32 ~ 57
// 주의: 문자열 비교 equals

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Node {
	int x;
	int y;
	int value;

	public Node(int x, int y, int value) {
		this.x = x;
		this.y = y;
		this.value = value;
	}
}

public class Main {
	static int N;
	static int[][] arr;
	static int[][] dist;
	static int INF = Integer.MAX_VALUE;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String input = "";
		int tc = 1;

		while (!(input = br.readLine()).equals("0")) {
			N = Integer.parseInt(input);
			arr = new int[N][N];
			dist = new int[N][N];

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					dist[i][j] = INF;
				}
			}

			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine().trim());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int result = dijkstra(0, 0);

			System.out.printf("Problem %d: %d\n", tc, result);
			tc++;
		}
	}

	public static int dijkstra(int i, int j) {
		int[] dx = { -1, 1, 0, 0 };
		int[] dy = { 0, 0, -1, 1 };

		PriorityQueue<Node> pQ = new PriorityQueue<>(Comparator.comparingInt(o -> o.value));
		Node root = new Node(i, j, arr[i][j]);
		pQ.offer(root);

		while (!pQ.isEmpty()) {
			Node now = pQ.poll();
			int x = now.x;
			int y = now.y;
			int value = now.value;

			// 더 최소면 skip
			if (dist[x][y] < value) continue;

			if (x == N - 1 && y == N - 1) {
				return value;
			}

			// 4방향으로 탐색해서 최소 루트 탐색
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if (isIn(nx, ny)) {
					int nextCost = value + arr[nx][ny];
					if (dist[nx][ny] > nextCost) {
						dist[nx][ny] = nextCost;
						pQ.offer(new Node(nx, ny, nextCost));
					}
				}
			}
		}

		return -1;

	}

	static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < N;
	}
}
