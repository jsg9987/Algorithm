import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static int V;
	static int E;
	static int[] indegree; // 노드 개수 + 1
	static List<List<Integer>> graph;

	public static void main(String[] args) throws IOException {
		int T = 10;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int tc = 1; tc < T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			V = Integer.parseInt(st.nextToken());
			E = Integer.parseInt(st.nextToken());
			indegree = new int[1001];
			graph = new ArrayList<>();

			for (int i = 0; i < V + 1; i++) {
				graph.add(new ArrayList<Integer>());
			}

			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < E; i++) {
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				graph.get(a).add(b);
				indegree[b] += 1; // 진입 차수 1 증가
			}
			
			topologySort(tc);
		}
	}

	// 위상 정렬
	public static void topologySort(int tc) {
		ArrayList<Integer> result = new ArrayList<>();

		Queue<Integer> q = new ArrayDeque<>();

		// 진입 차수가 0인 노드(graph의 idx)부터 큐에 삽입
		for (int i = 1; i < V + 1; i++) {
			if (indegree[i] == 0) {
				q.offer(i);
			}
		}

		while (!q.isEmpty()) {
			int node = q.poll();
			result.add(node); // 수행한 노드는 결과에 추가

			for (Integer e : graph.get(node)) {
				indegree[e] -= 1;

				if (indegree[e] == 0) {
					q.offer(e);
				}
			}
		}
		StringBuilder sb = new StringBuilder();
		for(Integer e : result) {
			sb.append(e).append(" ");
		}
		System.out.printf("#%d %s\n", tc, sb.toString());
	}
}
