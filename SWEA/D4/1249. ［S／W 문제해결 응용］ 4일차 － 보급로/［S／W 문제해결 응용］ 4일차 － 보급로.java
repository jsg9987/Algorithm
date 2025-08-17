
// 18:10 ~ 
// 20초, 256MB, tc:10, 1<=N<=100
// 

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;

class Node {
	int x, y, value;

	Node(int x, int y, int value) {
		this.x = x;
		this.y = y;
		this.value = value;
	}
}

public class Solution {
	static int N;
	static int[][] arr;
	static boolean[][] visited;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			N = Integer.parseInt(br.readLine().trim());
			arr = new int[N][N];
			visited = new boolean[N][N];

			for (int i = 0; i < N; i++) {
				String input = br.readLine().trim();
				for (int j = 0; j < N; j++) {
					arr[i][j] = input.charAt(j) - '0';
				}
			}

			int result = bfs(0, 0);

			System.out.printf("#%d %d\n", tc, result);
		}

	}

	static int bfs(int i, int j) {
		int[] dx = {-1,1,0,0};
		int[] dy = {0,0,-1,1};
		
		int val = arr[i][j];
		Node start = new Node(i,j,val);
		
		PriorityQueue<Node> pQ = new PriorityQueue<>(Comparator.comparingInt(o -> o.value));
		visited[i][j] = true;
		pQ.add(start);
		
		while(!pQ.isEmpty()) {
			Node now = pQ.poll();
			int x = now.x;
			int y = now.y;
			int value = now.value;
			if(x == N-1 && y == N-1) {
				return value;
			}
			
			for(int k = 0; k < 4; k++) {
				int nx = x + dx[k];
				int ny = y + dy[k];
				if(isIn(nx, ny) && !visited[nx][ny]) {
					visited[nx][ny] = true;
					pQ.add(new Node(nx, ny, value + arr[nx][ny]));
				}
			}
		}
		return 0;
	}
	
	static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < N && ny >= 0 && ny < N;
	}

}
