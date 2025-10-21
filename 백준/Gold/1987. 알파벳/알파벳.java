import java.io.*;
import java.util.*;

public class Main {
	static int R, C;
	static char[][] board;
	static boolean[] visited;
	static int[] dx = { -1, 0, 1, 0 };
	static int[] dy = { 0, 1, 0, -1 };
	static int result;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		result = 1;

		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		board = new char[R][C];
		for (int i = 0; i < R; i++) {
			String input = br.readLine().trim();
			for (int j = 0; j < C; j++) {
				board[i][j] = input.charAt(j);
			}
		}

		visited = new boolean[26];
		int firstCharIdx = board[0][0] - 'A';
		visited[firstCharIdx] = true;
		dfs(0, 0, result);

		// 결과 출력
		System.out.println(result);
	}

	private static void dfs(int x, int y, int cnt) {
		// 종료 조건: 더 이상 갈 곳이 없을 경우
		result = Math.max(result, cnt);

		// 유도 파트
		for (int dir = 0; dir < 4; dir++) {
			int nx = x + dx[dir];
			int ny = y + dy[dir];

			// 보드 안이고 방문하지 않았다면 재귀
			if (isIn(nx, ny)) {
				int nextCharIdx = board[nx][ny] - 'A'; //
				if (!visited[nextCharIdx]) {
					visited[nextCharIdx] = true;
					dfs(nx, ny, cnt + 1);
					visited[nextCharIdx] = false;
				}
			}
		}
	}

//	private static boolean canGo(int x, int y) {
//		boolean flag = false;
//		for (int dir = 0; dir < 4; dir++) {
//			System.out.println("들어왔음." + dir);
//			int nx = x + dx[dir];
//			int ny = y + dy[dir];
//
//			if (!isIn(nx, ny)) {
//				continue;
//			}
//
//			int nextCharIdx = board[nx][ny] - 'A';
//			System.out.println(nextCharIdx);
//			System.out.println(visited[nextCharIdx]);
//			if (!visited[nextCharIdx]) {
//				flag = true;
//			}
//		}
//
//		return flag;
//	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < R && ny >= 0 && ny < C;
	}
}