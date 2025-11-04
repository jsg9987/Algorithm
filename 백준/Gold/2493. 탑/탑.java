import java.io.*;
import java.util.*;

public class Main {
	static class Node {
		int idx;
		int volume;
		
		public Node(int idx, int volume) {
			this.idx = idx;
			this.volume = volume;
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine().trim()); // 탑의 수: 1 <= N <= 500_000
		int[] heights = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		// 높이 N개 입력 
		for(int i = 0; i < N; i++) {
			heights[i] = Integer.parseInt(st.nextToken());
		}
		int[] result = new int[N];
		Deque<Node> stack = new ArrayDeque<>();
		
		for(int i = N-1; i >= 0; i--) {
			Node temp = new Node(i, heights[i]);
			
			while(!stack.isEmpty() && stack.peekLast().volume < temp.volume) {
				Node cur = stack.pollLast();
				result[cur.idx] = i+1;
			}
			
			stack.add(temp);
		}
		
		for(int i = 0; i < N; i++) {
			bw.write(String.valueOf(result[i]));
			bw.write(" ");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}
}