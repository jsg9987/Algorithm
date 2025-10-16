import java.io.*;
import java.util.*;

public class Main {
	static int N, M, X;
	static int INF = 1_000_000_000;
	static List<ArrayList<Node>> map;
	static int[][] allDist;

	static class Node implements Comparable<Node> {
		int idx;
		int cost;

		public Node(int idx, int cost) {
			this.idx = idx;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node o) {
			return Integer.compare(this.cost, o.cost);
		}
	}

	static void dijkstra(int start) {
		PriorityQueue<Node> pQ = new PriorityQueue<>();
		Node first = new Node(start, 0);
		pQ.offer(first);

		int[] dist = new int[N];
		Arrays.fill(dist, INF);
		dist[start] = 0;

		while (!pQ.isEmpty()) {
			Node cur = pQ.poll();
			int idx = cur.idx;
			int cost = cur.cost;

			if (dist[idx] < cost)
				continue;

			for (Node e : map.get(idx)) {
				int to = e.idx;
				int toCost = e.cost;

				if (dist[idx] + toCost < dist[to]) {
					dist[to] = dist[idx] + toCost;
					pQ.offer(new Node(to, dist[idx] + toCost));
				}

			}
		}

		for (int i = 0; i < N; i++) {
			allDist[start][i] = dist[i];
		}
		
		return;
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		X = Integer.parseInt(st.nextToken()) - 1;
		map = new ArrayList<>();

		for (int i = 0; i < N; i++) {
			map.add(new ArrayList<>());
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int from = Integer.parseInt(st.nextToken()) - 1;
			int to = Integer.parseInt(st.nextToken()) - 1;
			int cost = Integer.parseInt(st.nextToken());

			map.get(from).add(new Node(to, cost));
		}

		allDist = new int[N][N];
		for (int i = 0; i < N; i++) {
			dijkstra(i);
		}
		
		int result = 0;
		for(int i = 0; i < N; i++) {
			result = Math.max(result, allDist[i][X] + allDist[X][i]);
		}
		
		bw.write(String.valueOf(result));
		bw.flush();
		bw.close();
		br.close();
	}
}