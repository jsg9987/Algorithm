import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim()); // 도시 개수 1 <= N <= 1,000
		int M = Integer.parseInt(br.readLine().trim()); // 버스의 개수 1 <= M <= 100,000
		int[][] graph = new int[N][N];
		boolean[] visited = new boolean[N];
		int INF = 100_000_000;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				if (i != j) {
					graph[i][j] = INF;
				}
			}
		}

		// 1. graph 초기화
		for (int i = 0; i < M; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int start = Integer.parseInt(st.nextToken()) - 1;
			int end = Integer.parseInt(st.nextToken()) - 1;
			int weight = Integer.parseInt(st.nextToken());

			graph[start][end] = Math.min(graph[start][end], weight);
		}

		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int start = Integer.parseInt(st.nextToken()) - 1;
		int end = Integer.parseInt(st.nextToken()) - 1;
		
		// 2. 시작 정점부터 시작
		int cnt = 0;
		visited[start] = true;
		while (true) { // cnt <= N
			int nextNode = -1;
			int tempMin = INF;
			
			for(int i = 0; i < N; i++) {
				if(visited[i]) continue;
				if(graph[start][i] < tempMin) {
					nextNode = i;
					tempMin = graph[start][i];
				}
			}
			
			if(nextNode == -1) break;
			visited[nextNode] = true;
//			cnt++;
			if(nextNode == end) break;
			
			// 3. 다음 루트 weight 갱신
			for(int i = 0; i < N; i++) {
				graph[start][i] = Math.min(graph[start][i], graph[start][nextNode] + graph[nextNode][i]);  
			}
		}
		
		System.out.println(graph[start][end]);
	}

}
