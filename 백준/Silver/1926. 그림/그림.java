import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
	static int n = 0;
	static int m = 0;
	static Deque<int[]> queue = new ArrayDeque<>();
	static boolean[][] visited = null;
	static int[][] arr = null;
	static int size = 0;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n][m];
		visited = new boolean[n][m];
		int maxCnt = 0;
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				int temp = Integer.parseInt(st.nextToken());
				arr[i][j] = temp;
			}
		}
		
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				if(arr[i][j] == 1 && !visited[i][j]) {
					int tempMax = bfs(i,j);
					if(maxCnt < tempMax) {
						maxCnt = tempMax;
					}
				}
			}
		}
		
		System.out.println(size);
		System.out.println(maxCnt);

	}

	public static boolean isin(int x, int y) {
		return x >= 0 && x < n && y >= 0 && y < m;
	}

	public static int bfs(int x, int y) {
		size++;
		int[] dx = { -1, 1, 0, 0 };
		int[] dy = { 0, 0, -1, 1 };
		queue.add(new int[] { x, y, 0 });
		int result = 1;
		visited[x][y] = true;
		
		while (!queue.isEmpty()) {
			// 그림이 그려진 좌표를 앞에서부터 빼서 bfs처리
			int[] p = queue.pollFirst();
			int j = p[0];
			int k = p[1];
			
			for (int i = 0; i < 4; i++) {
				int nx = j + dx[i];
				int ny = k + dy[i];
				if (isin(nx, ny) && !visited[nx][ny] && arr[nx][ny] == 1) {
					result++;
					visited[nx][ny] = true;
					queue.addFirst(new int[] { nx, ny });
				}
			}
		}
		
		return result;
	}
}
