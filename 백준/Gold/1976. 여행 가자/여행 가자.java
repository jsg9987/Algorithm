import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static int[] parents;
	static int[][] graph;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		N = Integer.parseInt(br.readLine()); // 도시의 수: 1 <= N <= 200
		M = Integer.parseInt(br.readLine()); // 계획에 속한 도시의 수: 1 <= M <= 1000
		// union find에서 부모 노드 배열 필요
		parents = new int[N];
		graph = new int[N][N];
		StringTokenizer st = null;
		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine().trim());
			for (int j = 0; j < N; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		// make()
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}

		// union()
		for (int i = 0; i < N; i++) {
			for (int j = i+1; j < N; j++) {
				if(graph[i][j] == 1) {
					union(i, j);
				}
			}
		}
		
		int[] route = new int[M];
		st = new StringTokenizer(br.readLine().trim());
		for(int i = 0; i < M; i++) {
			route[i] = Integer.parseInt(st.nextToken())- 1;
		}
		
		boolean result = true;
		for(int i =0; i < M-1; i++) {
			if(find(route[i]) != find(route[i+1])) { // 각 노드의 부모는 루트 부모와 다를 수 있음. find 함수로 같은 집합인지 체크해야함.
				result = false;
				break;
			}
		}
		
		if(result) {
			System.out.println("YES");
		}else {
			System.out.println("NO");
		}
	}

	// find: 자신이 속하는 집합을 찾음
	public static int find(int x) {
		if (parents[x] == x)
			return x;
		return parents[x] = find(parents[x]);
	}

	// union: 두 노드가 같은 집합에 속한다면 합치고 부모를 갱신
	public static boolean union(int x, int y) {
		int parentX = find(x);
		int parentY = find(y);

		if (parentX == parentY)
			return false;

		if (parentX <= parentY)
			parents[parentY] = parentX;
		else
			parents[parentX] = parentY;
		return true;
	}

}