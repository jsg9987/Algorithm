import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

/*
 * 4초, 256MB, 1<=n<=1,000,000 , 1<=m<=100,000
 */

public class Solution {
	static int N;
	static int[] parents;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine().trim());
		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			N = Integer.parseInt(st.nextToken());
			parents = new int[N+1];
			make();
			int M = Integer.parseInt(st.nextToken());
			sb.append("#").append(tc).append(" ");

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine().trim());
				int order = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				if (order == 0)
					union(a, b);
				else if (order == 1) {
					if (find(a, b))
						sb.append("1");
					else
						sb.append("0");
				}
			}
			sb.append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	static void make() {
		for (int i = 0; i < N+1; i++) {
			parents[i] = i;
		}
	}

	static int findRoot(int a) {
		if (parents[a] == a)
			return a;
		return parents[a] = findRoot(parents[a]); // 패스 압축 후
	}

	static boolean find(int a, int b) {
		int aRoot = findRoot(a);
		int bRoot = findRoot(b);
		if (parents[aRoot] == parents[bRoot])
			return true;
		return false;
	}

	static boolean union(int a, int b) {
		// 항상 각 노드의 루트노드가 누군지 찾아야함.
		int aRoot = findRoot(a);
		int bRoot = findRoot(b);

		// 만약 부모가 같다면 false
		if (parents[aRoot] == parents[bRoot])
			return false;
		// 아니면 bRoot 부모를 aRoot로 만들고 return true
		parents[bRoot] = aRoot;
		return true;
	}

}