import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Solution {
	static int N, W, H;
	static int minRemain;
	static int[][] board;
	static int[][] copy;
	static int[] numbers;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			N = Integer.parseInt(st.nextToken()); // 구슬 횟수
			W = Integer.parseInt(st.nextToken()); // 너비
			H = Integer.parseInt(st.nextToken()); // 높이
			board = new int[H][W];
			copy = new int[H][W];
			numbers = new int[N];
			
			for (int i = 0; i < H; i++) {
				st = new StringTokenizer(br.readLine().trim());
				for (int j = 0; j < W; j++) {
					board[i][j] = copy[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			minRemain = Integer.MAX_VALUE;

			perm(0);

			// 결과 출력
			sb.append("#").append(tc).append(" ").append(minRemain).append("\n");
		}

		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	static void perm(int cnt) {
		// 기저조건: N번 선택
		if (cnt == N) {
			// 탐색
			start(numbers);
			// 최소값 갱신
			minRemain = Math.min(minRemain, countBlock());
			// map 초기화
			boardCopy();
			return;
		}

		// x좌표 선택
		for (int i = 0; i < W; i++) {
			numbers[cnt] = i;
			perm(cnt + 1);
		}
	}

	static void start(int[] numbers) {
		int x = 0;
		int y = 0;

		// 각 차례마다 구슬을 떨어뜨리기
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < H; j++) { // 행을 이동해가며 부딪히는 좌표 찾기
				if (board[j][numbers[i]] != 0) {
					x = j;
					y = numbers[i];
					break;
				}
			}
			// bfs 후 벽돌 내리기
			bfs(x, y);
			blockDown();
		}
	}

	static void bfs(int x, int y) {
		Queue<int[]> q = new ArrayDeque<>();
		// 열에 블록 없을 경우 예외처리
		if(board[x][y] == 0) return;
		q.add(new int[] { x, y, board[x][y] });
		board[x][y] = 0;

		while (!q.isEmpty()) {
			int[] now = q.poll();
			int power = now[2];

			for (int i = 1; i < power; i++) {
				for (int j = 0; j < 4; j++) {
					int nx = now[0] + dx[j] * i;
					int ny = now[1] + dy[j] * i;

					// 범위 밖 or 블록 아닌 경우
					if (nx < 0 || nx >= H || ny < 0 || ny >= W || board[nx][ny] == 0) {
						continue;
					}

					if (board[nx][ny] != 0) {
						q.offer(new int[] { nx, ny, board[nx][ny] });
						board[nx][ny] = 0;
					}

				}
			}
		}
	}

	static void blockDown() {

		// 전체 배열에 대해서
		for (int i = 0; i < W; i++) {
			Stack<Integer> stack = new Stack<>();
			for (int j = 0; j < H; j++) {
				if (board[j][i] != 0) {
					stack.add(board[j][i]);
				}
			}

			for (int j = H - 1; j >= 0; j--) {
				if (stack.isEmpty())
					board[j][i] = 0;
				else
					board[j][i] = stack.pop();
			}
		}
	}
	
	static int countBlock() {
		int count = 0;
		
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				if(board[i][j] != 0) {
					count++;
				}
			}
		}
		
		return count;
	}
	
	static void boardCopy() {
		for(int i = 0; i < H; i++) {
			for(int j = 0; j < W; j++) {
				board[i][j] = copy[i][j];
			}
		}
	}

}