import java.io.*;

import java.util.*;

public class Main {

	static int[] dx = { -1, 0, 1, 0 };

	static int[] dy = { 0, 1, 0, -1 };

	static int R, C;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		R = Integer.parseInt(st.nextToken()); // 행,열: 1 <= R,C <= 1000
		C = Integer.parseInt(st.nextToken());
		char[][] miro = new char[R][C];
		boolean[][] fireVisited = new boolean[R][C];
		boolean[][] visited = new boolean[R][C];
		int start_x = -1;
		int start_y = -1;

		Queue<int[]> moveQ = new ArrayDeque<>();
		Queue<int[]> fireQ = new ArrayDeque<>();

		for (int i = 0; i < R; i++) {
			String s = br.readLine().trim();

			for (int j = 0; j < C; j++) {
				char temp = s.charAt(j);
				if (temp == 'J') {
					start_x = i;
					start_y = j;
					miro[i][j] = temp;
				} else if (temp == 'F') {
					fireQ.add(new int[] { i, j, 0 });
					fireVisited[i][j] = true;
					miro[i][j] = temp;
				} else {
					miro[i][j] = temp;
				}
			}
		}

		// 지훈이 큐에 삽입
		int result = -1;
		moveQ.add(new int[] { start_x, start_y, 0 });
		visited[start_x][start_y] = true;
		int time = 0;
		boolean flag = false;
		while (!moveQ.isEmpty() && !flag) {

			// 불 먼저
			while (!fireQ.isEmpty() && fireQ.peek()[2] == time) {
				int[] curFire = fireQ.poll();
				int x = curFire[0];
				int y = curFire[1];
				int cnt = curFire[2];

				for (int dir = 0; dir < 4; dir++) {
					int nx = x + dx[dir];
					int ny = y + dy[dir];
					if (isIn(nx, ny) && !fireVisited[nx][ny] && miro[nx][ny] != '#') {
						fireVisited[nx][ny] = true;
						miro[nx][ny] = 'F';
						fireQ.add(new int[] { nx, ny, cnt + 1 });
					}
				}
			}

			while (!moveQ.isEmpty() && moveQ.peek()[2] == time) {
				int[] cur = moveQ.poll();
				int x = cur[0];
				int y = cur[1];
				int cnt = cur[2];
				if (x == 0 || x == R - 1 || y == 0 || y == C - 1) {
					result = cnt + 1;
					flag = true;
					break;
				}

				for (int dir = 0; dir < 4; dir++) {
					int nx = x + dx[dir];
					int ny = y + dy[dir];

					if (isIn(nx, ny) && !visited[nx][ny] && miro[nx][ny] != '#' && miro[nx][ny] != 'F') {
						visited[nx][ny] = true;
						moveQ.add(new int[] { nx, ny, cnt + 1 });
					}
				}
			}

			time++;
		}

		if (result > 0) {
			bw.write(String.valueOf(result));
		} else {
			bw.write("IMPOSSIBLE");
		}
		bw.flush();
		bw.close();
		br.close();

	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < R && ny >= 0 && ny < C;
	}

}