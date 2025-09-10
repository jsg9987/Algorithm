import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int N;
	static int[][] board;
	static int shark_x, shark_y;
	static int shark_size;
	static int fishesEaten;
	static int endTime;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int INF = Integer.MAX_VALUE;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine().trim());
		shark_size = 2;
		fishesEaten = 0;
		board = new int[N][N];

		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < N; j++) {
				int temp = Integer.parseInt(st.nextToken());
				if (temp == 9) {
					shark_x = i;
					shark_y = j;
				}
				board[i][j] = temp;
			}
		}

		play();

		System.out.println(endTime);

	}

	private static void play() {

		while (true) {
			// 1. 먹을 수 있는 물고기 찾기
			List<int[]> small_fishes = new ArrayList<>();
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (board[i][j] != 9 && board[i][j] > 0 && board[i][j] < shark_size) {
						small_fishes.add(new int[] { i, j });
					}
				}
			}
			

			// 2. 가장 가까운 물고기 정하기 (x,y)
			int[] nextCoord = chooseNextFish(small_fishes);
			
			// 2.1 더 이상 먹을 물고기 없다면 종료
			if (nextCoord[0] == INF && nextCoord[1] == INF) {
				return;
			}
			

			// 3. 정했다면 이동시키기 -> 시간++, size 키워야하면 키우기
			move(nextCoord[0], nextCoord[1]);
			
		}
	}

	private static void move(int arrival_x, int arrival_y) {
		Queue<int[]> q = new ArrayDeque<>();
		boolean[][] visited = new boolean[N][N];
		visited[shark_x][shark_y] =true;
		q.offer(new int[] {shark_x, shark_y, endTime}); // x,y,시간
		
		while(!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			int time = cur[2];
			
			if(x == arrival_x && y == arrival_y) {
				board[shark_x][shark_y] = 0;
				board[x][y] = 9;
				shark_x = x;
				shark_y = y;
				endTime = time;
				fishesEaten++;
				if(shark_size == fishesEaten) {
					shark_size++;
					fishesEaten = 0;
				}
				break;
			}
			
			for(int dir = 0; dir < 4; dir++) {
				int nx = x + dx[dir];
				int ny = y + dy[dir];
				if(isIn(nx, ny) && !visited[nx][ny] && board[nx][ny] <= shark_size) {
					visited[nx][ny] = true;
					q.offer(new int[] {nx, ny, time + 1});
				}
			}
		}
	}

	private static int[] chooseNextFish(List<int[]> small_fishes) {
		int[] nextCoord = new int[2];
		int minDist = Integer.MAX_VALUE;
		List<int[]> candidates = new ArrayList<>();
		
		for (int[] e : small_fishes) {
			Queue<int[]> q = new ArrayDeque<int[]>();
			boolean[][] visited = new boolean[N][N];
			visited[shark_x][shark_y] = true;
			q.offer(new int[] {shark_x, shark_y, 0});
			
			while(!q.isEmpty()) {
				int[] cur = q.poll();
				int x = cur[0];
				int y = cur[1];
				int dist = cur[2];
				
				if(x == e[0] && y == e[1]) { // 먹을 수 있는 물고기에 도착했다면 종료
					candidates.add(new int[] {x,y,dist});
					break;
				}
				
				for(int dir = 0; dir < 4; dir++) {
					int nx = x + dx[dir];
					int ny = y + dy[dir];
					
					if(isIn(nx, ny) && !visited[nx][ny] &&board[nx][ny] <= shark_size) { // 자기보다 큰 물고기가 막고있다면 이동 불가
						visited[nx][ny] = true;
						q.offer(new int[] {nx, ny, dist+1});
					}
				}
			}
		}
		
		Collections.sort(candidates, (o1, o2) -> (o1[2] == o2[2]) ? ((o1[0] == o2[0]) ? Integer.compare(o1[1], o2[1]): Integer.compare(o1[0], o2[0])): Integer.compare(o1[2], o2[2]));
		
		if(candidates.isEmpty()) {
			return new int[] {INF, INF}; 
		}
		return candidates.get(0);
	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < N && ny >= 0 && ny < N;
	}
}