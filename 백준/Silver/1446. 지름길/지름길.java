import java.io.*;
import java.util.*;

public class Main {

	public static class Road implements Comparable<Road> {
		int from;
		int to;
		int length;

		public Road(int from, int to, int length) {
			this.from = from;
			this.to = to;
			this.length = length;
		}

		@Override
		public int compareTo(Road o) {
			return Integer.compare(this.to, o.to);
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		int N = Integer.parseInt(st.nextToken());
		int D = Integer.parseInt(st.nextToken());
		int[] DP = new int[D + 1];
		for (int j = 0; j < D + 1; j++) {
			DP[j] = j;
		}

		ArrayList<Road> roads = new ArrayList<>();
		for (int i = 1; i < N + 1; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int from = Integer.parseInt(st.nextToken());
			int to = Integer.parseInt(st.nextToken());
			int length = Integer.parseInt(st.nextToken());

			if (to > D || length > to - from) {
				continue;
			}

			roads.add(new Road(from, to, length));
		}

		Collections.sort(roads);
		
		for(int i = 1; i < D+1; i++) {
			DP[i] = Math.min(DP[i], DP[i-1] + 1);
			
			for(Road road : roads) {
				if(road.to == i) {
					int shortcut = DP[road.from] + road.length;
					DP[i] = Math.min(DP[i], shortcut);
				}
			}
		}

		System.out.println(DP[D]);
	}
}