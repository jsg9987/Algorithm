import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
	static int N;
	static int[][] board;
	static StringBuilder sb;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		sb = new StringBuilder();

		N = Integer.parseInt(br.readLine().trim()); // N 길이 1 <= N <= 64
		board = new int[N][N];

		for (int i = 0; i < N; i++) {
			String input = br.readLine().trim();
			for (int j = 0; j < N; j++) {
				board[i][j] = input.charAt(j) - '0';
			}
		}

		divide_conq(N, 0, 0);
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	static void divide_conq(int N, int start_x, int start_y) {
		boolean flag = true;
		int firstValue = board[start_x][start_y];
		// 기저 조건: 범위 내에 모두 같은 숫자
		for (int i = start_x; i < start_x + N; i++) {
			for (int j = start_y; j < start_y + N; j++) {
				if (board[i][j] != firstValue) {
					flag = false;
					break;
				}
			}
			if (!flag)
				break;
		}

		// String에 합치고 종료
		if (flag) {
			sb.append(firstValue);
			return;
		}

		// 네 군데로 다시 분할정복
		int half = N / 2;
		sb.append("(");
		divide_conq(half, start_x, start_y);
		divide_conq(half, start_x, start_y + half);
		divide_conq(half, start_x + half, start_y);
		divide_conq(half, start_x + half, start_y + half);
		sb.append(")");

	}
}