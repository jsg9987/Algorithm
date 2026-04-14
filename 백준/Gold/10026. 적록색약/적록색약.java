import java.io.*;
import java.util.*;

public class Main {
	public static int N;
	public static int[][] board;
	public static boolean[][] visited;
	public static int[] dx = new int[] { -1, 0, 1, 0 };
	public static int[] dy = new int[] { 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		N = Integer.parseInt(br.readLine().trim());
		board = new int[N][N];
		visited = new boolean[N][N];
		int normal_result = 0;
		int red_green_result = 0;

		for (int i = 0; i < N; i++) {
			String input = br.readLine().trim();
			for (int j = 0; j < input.length(); j++) {
				board[i][j] = input.charAt(j);
			}
		}

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					normal_bfs(i, j);
					normal_result++;
				}
			}
		}

		visited = new boolean[N][N];

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (!visited[i][j]) {
					red_green_bfs(i, j);
					red_green_result++;
				}
			}
		}

		bw.write(String.valueOf(normal_result));
		bw.write('\n');
		bw.write(String.valueOf(red_green_result));
		bw.flush();
		bw.close();
		br.close();
	}

	public static void normal_bfs(int x, int y) {
		Queue<int[]> q = new ArrayDeque<>();

		q.offer(new int[] { x, y });
		visited[x][y] = true;
		int color = board[x][y];

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			x = cur[0];
			y = cur[1];

			for (int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				if (isIn(nx, ny) && !visited[nx][ny] && board[nx][ny] == board[x][y]) {
					visited[nx][ny] = true;
					q.offer(new int[] { nx, ny });
				}
			}
		}
	}

	public static void red_green_bfs(int x, int y) {
		Queue<int[]> q = new ArrayDeque<>();

		q.offer(new int[] { x, y });
		visited[x][y] = true;
		int color = board[x][y];

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			x = cur[0];
			y = cur[1];

			for (int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				
				// 적색-녹색, 녹색-적색으로 붙어있다면 BFS 더 퍼질 수 있음.
				if (isIn(nx, ny) && !visited[nx][ny] && (board[nx][ny] == board[x][y]
						|| (board[nx][ny] == 'R' && board[x][y] == 'G')
						|| (board[nx][ny] == 'G' && board[x][y] == 'R'))) {
					visited[nx][ny] = true;
					q.offer(new int[] { nx, ny });
				}
			}
		}
	}

	public static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < N;
	}
}