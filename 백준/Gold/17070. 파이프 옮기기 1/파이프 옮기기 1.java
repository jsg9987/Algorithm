import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] board;
	static int result;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine().trim());
		board = new int[N][N];

		// 판 초기화
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < N; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		dfs(0, 1, 0); // x,y, 방향(가로,대각,세로)

		System.out.println(result);

	}

	private static void dfs(int i, int j, int dir) {
		// 기저 조건: (N-1,N-1)에 도착했을 때
		if(i == N-1 && j == N-1) {
			result++;
			return;
		}

		// 유도 파트: 방향에 따라서 갈 수 있는 다음 위치로 이동해보기, 벽이면 못가게한다.
		if (dir == 0) {
			if (isIn(i, j + 1) && board[i][j + 1] != 1) {
				dfs(i, j + 1, 0);
			}
			if (isIn(i + 1, j + 1) && board[i + 1][j + 1] != 1 && board[i][j+1] != 1 && board[i+1][j] != 1) {
				dfs(i + 1, j + 1, 1);
			}
		} else if (dir == 1) {
			if (isIn(i, j + 1) && board[i][j + 1] != 1) {
				dfs(i, j + 1, 0);
			}
			if (isIn(i + 1, j + 1) && board[i + 1][j + 1] != 1 && board[i][j+1] != 1 && board[i+1][j] != 1) {
				dfs(i + 1, j + 1, 1);
			}
			if (isIn(i + 1, j) && board[i + 1][j] != 1) {
				dfs(i + 1, j, 2);
			}
		} else if (dir == 2) {
			if (isIn(i + 1, j + 1) && board[i + 1][j + 1] != 1 && board[i][j+1] != 1 && board[i+1][j] != 1) {
				dfs(i + 1, j + 1, 1);
			}
			if (isIn(i + 1, j) && board[i + 1][j] != 1) {
				dfs(i + 1, j, 2);
			}
		}

	}

	private static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < N;
	}

}