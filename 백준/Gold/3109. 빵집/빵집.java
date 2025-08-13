import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	static int R;
	static int C;
	static char[][] arr;
	static boolean[][] visited;
	static int[][] move = new int[][] { { -1, 1 }, { 0, 1 }, { 1, 1 } };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		R = Integer.parseInt(st.nextToken());
		C = Integer.parseInt(st.nextToken());
		arr = new char[R][C];
		visited = new boolean[R][C];
		int result = 0;

		for (int i = 0; i < R; i++) {
			String input = br.readLine();
			for (int j = 0; j < C; j++) {
				arr[i][j] = input.charAt(j);
			}
		}

		// best 찾기
		for (int i = 0; i < R; i++) {
			visited[i][0] = true;
			dfs(i, 0);
		}

		for (int i = 0; i < R; i++) {
			if (visited[i][C - 1]) {
				result++;
			}
		}

		System.out.println(result);
	}

	public static boolean dfs(int row, int col) {
		// 마지막 열에 도착 시 true
		if (col == C - 1) {
			// 디버깅
//			for(boolean[] arr1 : visited) {
//				System.out.println(Arrays.toString(arr1));
//			}
//			System.out.println();
			return true;
		}

		// 3가지 화살표로 재귀
		for (int i = 0; i < 3; i++) {
			int nr = row + move[i][0];
			int nc = col + move[i][1];
			if (isPossible(nr, nc)) {
				visited[nr][nc] = true;
				if(dfs(nr, nc)) {
					return true;
				}
//				else {
//					visited[nr][nc] = false;
//				}
			}
		}
		// 더 이상 못가면 false return
		return false;
	}

	public static boolean isPossible(int x, int y) {
		return x >= 0 && x < R && y >= 0 && y < C && arr[x][y] != 'x' && !visited[x][y];
	}
}
