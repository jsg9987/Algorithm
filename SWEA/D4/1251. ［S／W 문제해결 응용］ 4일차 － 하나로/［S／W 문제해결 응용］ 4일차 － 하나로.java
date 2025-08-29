import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution {

	static class Edge implements Comparable<Edge> {
		int from, to;
		long weight;

		public Edge(int from, int to, long weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return Long.compare(this.weight, o.weight);
		}

		@Override
		public String toString() {
			return "Edge [from=" + from + ", to=" + to + ", weight=" + weight + "]";
		}
	}

	static int N;
	static Edge[] edges;
	static int[] parents;

	static void make() {
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}
	}

	static int findRoot(int a) {
		if (parents[a] == a)
			return a;
		return parents[a] = findRoot(parents[a]);
	}

	static boolean union(int a, int b) {
		int aRoot = findRoot(a);
		int bRoot = findRoot(b);

		if (aRoot == bRoot)
			return false; // 부모가 같으면 간선 이으면 사이클됨.

		if (aRoot > bRoot)
			parents[bRoot] = aRoot;
		else
			parents[aRoot] = bRoot;
		return true;
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 1; tc < T + 1; tc++) {
			N = Integer.parseInt(br.readLine().trim());
			edges = new Edge[N * (N - 1) / 2];
			parents = new int[N];
			ArrayList<long[]> xy = new ArrayList<>();
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			StringTokenizer st2 = new StringTokenizer(br.readLine().trim());
			
			for (int i = 0; i < N; i++) {
				xy.add(new long[] { Long.parseLong(st.nextToken()), Long.parseLong(st2.nextToken()) });
			}

			// 간선 초기화 -> Point Class로도 가능
			int edgeSize = 0;
			for (int i = 0; i < N - 1; i++) {
				for (int j = i + 1; j < N; j++) {
					if(edgeSize == edges.length) break;
					long[] xy1 = xy.get(i);
					long[] xy2 = xy.get(j);
					long dx = Math.abs(xy1[0] - xy2[0]);
					long dy = Math.abs(xy1[1] - xy2[1]);
					edges[edgeSize] = new Edge(i, j, dx * dx + dy * dy);
					edgeSize++;
				}
			}

			// 간선 오름차순 정렬
			Arrays.sort(edges);
//			System.out.println(Arrays.toString(edges));
			// 1. 모두 서로소 집합으로 만들고
			make();

			// 2. 가장 짧은 것부터 선택하며 사이클을 만들지 않으면 union, V-1개 고르면 end
			double result = 0;
			int cnt = 0;
			for (Edge edge : edges) {
				if (!union(edge.from, edge.to))
					continue;

				// 합칠 수 있을 때
				result += edge.weight;
			}
			double E = Double.parseDouble(br.readLine().trim());// 세율 실수 E 0 <= E <= 1
			result *= E;
			
			System.out.printf("#%d %d\n", tc, Math.round(result));

		}
	}

}