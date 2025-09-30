import java.io.*;
import java.util.*;

public class Main {
	static int INF = 100_000_000;
	static int minValue;
	static int W, H, K;
	static boolean[][][] visited;
	static int[][] graph; 
	static int[][] dir = new int[][] { { 1, 2 }, { 2, 1 }, { 2, -1 }, { 1, -2 }, { -1, -2 }, { -2, -1 }, { -2, 1 },
			{ -1, 2 }, { 1, 0 }, { 0, 1 }, { -1, 0 }, { 0, -1 }, };

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		K = Integer.parseInt(br.readLine().trim());
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		W = Integer.parseInt(st.nextToken());
		H = Integer.parseInt(st.nextToken());
		graph = new int[H][W];

		for (int i = 0; i < H; i++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < W; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		visited = new boolean[H][W][K+1];

		minValue = -1;
		bfs(0, 0, K, 0);
		
		System.out.println(minValue);
	}

	private static void bfs(int i, int j, int k, int l) {
		Queue<int[]> q = new ArrayDeque<>();
		q.offer(new int[] { i, j, k, l });

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			int x = cur[0];
			int y = cur[1];
			int remainK = cur[2];
			int cnt = cur[3];

			if (x == H - 1 && y == W - 1) {
				minValue = cnt;
				break;
			}

			for (int d = 0; d < 12; d++) {
				int nx = x + dir[d][0];
				int ny = y + dir[d][1];
				if (isIn(nx, ny) && graph[nx][ny] != 1) {
					if(d < 8 && remainK-1 >= 0 &&!visited[nx][ny][remainK-1]) {
						visited[nx][ny][remainK-1] = true;
						q.offer(new int[] {nx, ny, remainK-1, cnt+1});
					}else if(d >= 8 && remainK >= 0 && !visited[nx][ny][remainK]) {
						visited[nx][ny][remainK] = true;
						q.offer(new int[] {nx, ny, remainK, cnt+1});
					}
				}
			}
		}
	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < H && ny >= 0 && ny < W;
	}
}
