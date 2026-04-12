import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M, K;
	static char[][] board;
	static int start_x, start_y, end_x, end_y;
	static int[][] minTime;
	static int[] dx = { -1, 1, 0, 0 }; // 상, 하, 좌, 우
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		board = new char[N][M];
		minTime = new int[N][M];

		for (int i = 0; i < N; i++) {
			String input = br.readLine().trim();
			for (int j = 0; j < M; j++) {
				board[i][j] = input.charAt(j);
			}
		}

		// minTime 배열을 최대값으로 초기화
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				minTime[i][j] = Integer.MAX_VALUE;
			}
		}

		// 좌표 입력 (1-based index이므로 0-based로 변환)
		st = new StringTokenizer(br.readLine().trim());
		start_x = Integer.parseInt(st.nextToken()) - 1;
		start_y = Integer.parseInt(st.nextToken()) - 1;
		end_x = Integer.parseInt(st.nextToken()) - 1;
		end_y = Integer.parseInt(st.nextToken()) - 1;

		int result = bfs(start_x, start_y);

		System.out.println(result);
	}

	static int bfs(int start_x, int start_y) {
		Queue<int[]> q = new ArrayDeque<>();
		minTime[start_x][start_y] = 0;
		q.offer(new int[] { start_x, start_y });

		while (!q.isEmpty()) {
			int[] now = q.poll();
			int x = now[0];
			int y = now[1];
			int time = minTime[x][y];

			if (x == end_x && y == end_y) {
				return time;
			}

			// 4가지 방향으로 슬라이드 시작
			for (int dir = 0; dir < 4; dir++) {
				// 각 방향으로 최대 K칸까지 '한 칸씩' 나아가며 탐색
				for (int k = 1; k <= K; k++) {
					int nx = x + dx[dir] * k;
					int ny = y + dy[dir] * k;

					// 1. 맵 밖으로 벗어나거나 벽을 만나면, 이 방향으로는 더 이상 진행 불가
					if (!isIn(nx, ny) || board[nx][ny] == '#') {
						break; // 이 방향의 슬라이드를 중단
					}

					// 2. 만약 이미 더 빠른 경로가 발견된 지점이라면, 현재 경로는 더 볼 필요 없음
					if (minTime[nx][ny] < time + 1) {
						break; // 이 방향의 슬라이드를 중단
					}

					// 3. 만약 다른 경로가 같은 시간으로 이미 방문했다면, 큐에 중복 추가할 필요 없음
					// 하지만 그 지점을 '통과'해서 더 멀리 갈 수는 있으므로 슬라이드는 계속
					if (minTime[nx][ny] == time + 1) {
						continue;
					}

					// 4. 새로운 최단 경로를 발견한 경우
					minTime[nx][ny] = time + 1; // 최소 시간 갱신
					q.offer(new int[] { nx, ny }); // 다음 탐색을 위해 큐에 추가
				}
			}
		}

		return -1; // 도착점에 도달할 수 없는 경우
	}

	// 맵의 범위 안에 있는지 확인하는 함수
	static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < M;
	}
}