import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

// 핵심 아이디어: root 노드를 처음으로 bfs 탐색하여 depth가 2 이하인 자식 노드만 count해서 동기를 구하자.
// 
public class Main {
	static int result = 0;
	static boolean[] visited = null;
	static List<List<Integer>> graph = null;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int m = Integer.parseInt(br.readLine());
		visited = new boolean[n];
		graph = new ArrayList<>();
		for (int i = 0; i < n; i++) {
			graph.add(new ArrayList<>());
		}

		for (int i = 0; i < m; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken()) - 1;
			int b = Integer.parseInt(st.nextToken()) - 1;

			graph.get(a).add(b);
			graph.get(b).add(a);
		}

		// 그래프 노드 디버깅
//		for (List<Integer> e : graph) {
//			System.out.println(e.toString());
//		}

		bfs(0);
		System.out.println(result);

	}

	public static void bfs(int start) {
		Queue<int[]> q = new ArrayDeque<>();
		q.add(new int[] { start, 0 });
		visited[start] = true;

		while (!q.isEmpty()) {
			int[] node = q.poll();
			int nodeIdx = node[0];
			int depth = node[1];

			for (int i = 0; i < graph.get(nodeIdx).size(); i++) {
				int nextIdx = graph.get(nodeIdx).get(i);
				if (!visited[nextIdx] && depth < 2) {
					result++;
					visited[nextIdx] = true;
					q.add(new int[] {nextIdx, depth + 1});
				}
			}
		}

	}
}
