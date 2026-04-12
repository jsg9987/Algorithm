import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		List<int[]> graph = new ArrayList<int[]>();
		int[] DP = new int[501];
		int[] lastElement = new int[501];
		StringTokenizer st = null;

		for (int i = 0; i < N; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());

			graph.add(new int[] { from, to });
		}

		Collections.sort(graph, (o1, o2) -> Integer.compare(o1[0], o2[0]));

		for (int[] e : graph) {
			int a = e[0];
			int b = e[1];
//			System.out.println("a,b:" + a + " " +b);
			lastElement[a] = b;

			DP[a] = DP[0] + 1;
			for (int i = 0; i < a; i++) {
				if (lastElement[a] > lastElement[i]) {
					DP[a] = Math.max(DP[i] + 1, DP[a]);
				}
			}
		}

		int LIS_length = 0;
		for (int i = 0; i < DP.length; i++) {
			LIS_length = Math.max(LIS_length, DP[i]);
		}
		
		System.out.println(N-LIS_length);
	}
}