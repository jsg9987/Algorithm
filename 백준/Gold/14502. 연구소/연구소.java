import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N, M;
	static int[][] board;
	static int[][] copy;
	static List<int[]> virusCoords;
	static int[][] blankCoords;
	static int maxValue;
	static boolean[] visited;
	static int idx;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static boolean[][] copyVisited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		board = new int[N][M];
		copy = new int[N][M];
		maxValue = 0;
		virusCoords = new ArrayList<int[]>();
		copyVisited = new boolean[N][M];

		// board 초기화
		idx = 0;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < M; j++) {
				int temp = Integer.parseInt(st.nextToken());
				if (temp == 0) {
					idx++;
				}
				board[i][j] = temp;
			}
		}

		blankCoords = new int[idx][2];
		visited = new boolean[idx];
//		System.out.println("idx: " + idx);
		idx = 0;

		// 0좌표 저장, 바이러스 좌표 저장, 벽은 못퍼짐
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (board[i][j] == 0) {
					blankCoords[idx][0] = i;
					blankCoords[idx][1] = j;
					idx++;
				} else if (board[i][j] == 2) {
					virusCoords.add(new int[] { i, j });
				}
			}
		}

		// copy 배열 복사
		for (int i = 0; i < N; i++) {
			copy[i] = board[i].clone();
		}

		dfs(0);

		// 결과 출력
//		bw.write(maxValue);
//		bw.flush();
		System.out.println(maxValue);
		bw.close();
		br.close();

	}

	private static void dfs(int selectedCnt) {
		// 기저 조건: 3개 골랐을 때 bfs하고 최댓값 갱신, copy 초기화, return
		if (selectedCnt == 3) {
			bfs();
//			for(int i = 0; i < N; i++) {
//				System.out.println(Arrays.toString(copy[i]));
//			}
//			for(int i = 0; i < N; i++) {
//				System.out.println(Arrays.toString(board[i]));
//			}
			
			for(int i = 0; i < N; i++) {
				copy[i] = board[i].clone();
			}
			copyVisited = new boolean[N][M];
			return;
		}

		// 유도 파트: 조합(3개 선택)
		for (int i = 0; i < idx; i++) {
			if (!visited[i]) {
				visited[i] = true;
				selectedCnt++;
				dfs(selectedCnt);
				selectedCnt--;
				visited[i] = false;
			}
		}
	}

	private static void bfs() {
		// 벽 3개 세우기
		for (int i = 0; i < idx; i++) {
			if (visited[i]) {
				int x = blankCoords[i][0];
				int y = blankCoords[i][1];
				copy[x][y] = 1;
			}
		}
		
		Queue<int[]> q = new ArrayDeque<>();
		for(int[] e : virusCoords) {
			copyVisited[e[0]][e[1]] = true;
			q.offer(e);
		}
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			
			for(int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				
				if(isIn(nx, ny) && copy[nx][ny] != 1 && !copyVisited[nx][ny]) {
					copyVisited[nx][ny] = true;
					copy[nx][ny] = 2;
					q.offer(new int[] {nx, ny});
				}
			}
		}
		
		int safeCnt = 0;
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				if(copy[i][j] == 0) {
					safeCnt++;
				}
			}
		}
		
		maxValue = Math.max(maxValue, safeCnt);
	}
	
	static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < M;
	}

}