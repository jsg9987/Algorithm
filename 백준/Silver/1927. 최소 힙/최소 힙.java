import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		PriorityQueue<Integer> pQ = new PriorityQueue<>();

		int N = Integer.parseInt(br.readLine().trim());
		for (int i = 0; i < N; i++) {
			int x = Integer.parseInt(br.readLine().trim());
			if (x == 0) {
				if (pQ.isEmpty()) {
					System.out.println(0);
				} else {
					System.out.println(pQ.poll());
				}
			} else {
				pQ.offer(x);
			}
		}
	}
}
