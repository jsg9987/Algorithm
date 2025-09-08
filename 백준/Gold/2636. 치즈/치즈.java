import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[][] board;
//	static boolean[][] visited;
	static int resultTime, cheeseCnt;
	static Queue<int[]> cheese_exteriors;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][M];
//		visited = new boolean[N][M];
		resultTime = 0;
		cheeseCnt = 0;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < M; j++) {
				board[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		cheeseCnt = simulation();

		System.out.println(resultTime);
		System.out.println(cheeseCnt);

	}

	private static int simulation() {
		int time = 0;

		while (true) {
			boolean endFlag = true;
			cheese_exteriors = new ArrayDeque<>();

			// 0. 모두 녹을 치즈인지 확인
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					if (board[i][j] == 1) {
						endFlag = false;
					} else if (board[i][j] == 3) {
						cheese_exteriors.offer(new int[] { i, j });
					}
				}
			}
			
//			System.out.println("0. 넘어감");
			// 1. 모두 녹을 치즈라면(한 시간 후에 끝나는 상태라면), 치즈 개수 세고 time + 1 return
			if (endFlag) {
				int cheeseCnt = 0;
				for(int i = 0; i < N; i++) {
					for(int j = 0; j < M; j++) {
						if(board[i][j] == 3) {
							cheeseCnt++;
						}
					}
				}
				
				resultTime = time;
				return cheeseCnt;
			}
			
//			System.out.println("1. 넘어감");
			// 2. 녹을 치즈 녹이기
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < M; j++) {
					if(board[i][j] == 3) {
						board[i][j] = 0;
					}
				}
			}
			
			// 3. 첫 번째 공기 칸에서 bfs해서 구멍에 공기 들어가게하기, 다음 시간에 녹을 치즈 결정
			bfs(0,0);
//			System.out.println("3. 넘어감");
			
			// 4. 시간 늘리기
			time++;

		}

	}

	private static void bfs(int i, int j) {
		boolean[][] localVisited = new boolean[N][M];
		Queue<int[]> q = new ArrayDeque<>();
		localVisited[i][j] = true;
		q.offer(new int[] {i,j});
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			
			for(int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				
				// 공기인 경우 -> 겉면 치즈를 찾기 위해 큐에 넣어줌
				if(isIn(nx, ny) && !localVisited[nx][ny] && board[nx][ny] == 0) {
					localVisited[nx][ny] = true;
					q.offer(new int[] {nx, ny});
				}else if(isIn(nx, ny) && !localVisited[nx][ny] && board[nx][ny] == 1) {
					localVisited[nx][ny] = true;
					board[nx][ny] = 3;
				}
			}
		}
		
		
		
		
	}
	
//	private static int countCheese(Queue<int[]> cheese_exteriors) {
//		boolean[][] visited = new boolean[N][M];
//		int result = 0;
//
//		while (!cheese_exteriors.isEmpty()) {
//			Queue<int[]> tempQ = new ArrayDeque<>();
//			int[] cur = cheese_exteriors.poll();
//			int x = cur[0];
//			int y = cur[1];
//
//			if (visited[x][y])
//				continue;
//			visited[x][y] = true;
//			tempQ.offer(new int[] { x, y });
//			result++;
//
//			while (!tempQ.isEmpty()) {
//				int[] cur2 = tempQ.poll();
//				int cx = cur2[0];
//				int cy = cur2[1];
//				
//				for (int dir = 0; dir < 4; dir++) {
//					int nx = cx + dx[dir];
//					int ny = cy + dy[dir];
//
//					if (isIn(nx, ny) && !visited[nx][ny] && board[nx][ny] == 3) {
//						visited[nx][ny] = true;
//						tempQ.offer(new int[] {nx,ny});
//					}
//				}
//			}
//
//		}
//		
//		return result;
//	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < N && ny >= 0 && ny < M;
	}
}