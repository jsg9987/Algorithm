import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

// 2초, 256MB, tc: 27, 1<=N<=1000
// 출발 가능점들을 뽑아서 bfs

public class Solution {
	static int N;
	static int[][] arr;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };
	static int maxResult;
	static int minRoomNum;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			N = Integer.parseInt(br.readLine().trim());
			maxResult = 0;
			minRoomNum = Integer.MAX_VALUE;
			arr = new int[N][N];
			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine().trim());
				for (int j = 0; j < N; j++) {
					arr[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			Queue<int[]> xy = new ArrayDeque<>();

			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					boolean flag = true;
					for (int d = 0; d < 4; d++) {
						int nx = i + dx[d];
						int ny = j + dy[d];
						if (isIn(nx, ny)) {
							if (arr[nx][ny] == arr[i][j] - 1) {
								flag = false;
								break;
							}
						}
					}
					if (flag)
						xy.offer(new int[] { i, j });
				}
			}

			int result_x, result_y;

			while (!xy.isEmpty()) {
				int[] now = xy.poll();
				int x = now[0];
				int y = now[1];
				bfs(x, y);
			}

			System.out.printf("#%d %d %d\n", tc, minRoomNum, maxResult);
		}
	}

	static void bfs(int x, int y) {
		int cnt = 1;
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[] { x, y });

		while (!q.isEmpty()) {
			int[] now = q.poll();
			int now_x = now[0];
			int now_y = now[1];
			for (int d = 0; d < 4; d++) {
				int nx = now_x + dx[d];
				int ny = now_y + dy[d];
				if (isIn(nx, ny)) {
					if (arr[nx][ny] == arr[now_x][now_y] + 1) {
						cnt += 1;
						q.offer(new int[] {nx, ny});
					}
				}
			}
		}

		if (cnt == maxResult) {
			if (minRoomNum > arr[x][y]) {
				minRoomNum = arr[x][y];
			}
		} else if (cnt > maxResult) {
			maxResult = cnt;
			minRoomNum = arr[x][y];
		}
	}

	static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < N;
	}
}