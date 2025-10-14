import java.io.*;
import java.util.*;

public class Main {
	static int M, N;
	static int[][] board;
	static int mass;
	static boolean[][] visited;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,1,0,-1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		M = Integer.parseInt(st.nextToken());
		N = Integer.parseInt(st.nextToken());
		board = new int[M][N];
		mass = 0;

		for (int i = 0; i < M; i++) {
			String input = br.readLine().trim();
			for (int j = 0; j < N; j++) {
				int temp = input.charAt(j) - '0';
				board[i][j] = temp;
			}
		}

		int day = 0;
		while (true) {
			
			// 1. 한 덩어리의 곰팡이인지 체크
			mass = 0;
			visited = new boolean[M][N];
			for(int i = 0; i < M; i++) {
				for(int j = 0; j < N; j++) {
					if(board[i][j] > 0 && !visited[i][j]) {
						bfs(i, j);
						mass++;
					}
				}
			}
			
			if(mass == 1) {
				break;
			}
			
//			System.out.println("--- 출력---");
//			for(int i = 0; i < M; i++) {
//				System.out.println(Arrays.toString(board[i]));
//			}
//			System.out.println("---출력 끝---");

			// 2.1 배열 복사해서 방금 퍼진 곰팡이 또 못퍼지게
			int[][] copy = new int[M][N];
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < N; j++) {
					copy[i][j] = board[i][j];
				}
			}

			// 2.2 모든 0이 아닌 칸에서 곰팡이를 퍼뜨림.
			for (int i = 0; i < M; i++) {
				for (int j = 0; j < N; j++) {
					int growSpeed = board[i][j];
					if (growSpeed != 0) { // 곰팡이 있다면
						// 자라는 속도 K에 맞게 곰팡이 퍼뜨린다.
						for (int xK = -growSpeed; xK <= growSpeed; xK++) {
							for (int yK = -growSpeed; yK <= growSpeed; yK++) {
								// 만약 곰팡이가 퍼질 수 있는 칸이면 채운다.
								if (isIn(i+xK, j+yK) && growSpeed > copy[i + xK][j + yK]) {
									copy[i + xK][j + yK] = growSpeed;
								}
							}
						}
					}
				}
			}
			
			// 2.3 원본 배열에 다시 대입
			board = copy;
			
			// 3. 하루 추가
			day++;
		}
		
		System.out.println(day);

	}

	private static void bfs(int i, int j) {
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[] {i,j});
		visited[i][j] = true;
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			
			for(int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				
				if(isIn(nx, ny) && !visited[nx][ny] && board[nx][ny] > 0) {
					q.offer(new int[] {nx, ny});
					visited[nx][ny] = true;
				}
			}
		}
	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < M && ny >= 0 && ny < N;
	}
}