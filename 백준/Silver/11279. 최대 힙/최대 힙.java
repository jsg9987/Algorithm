import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.PriorityQueue;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		PriorityQueue<Integer> pQ = new PriorityQueue<>(Collections.reverseOrder());

		for (int i = 0; i < N; i++) {
			int x = Integer.parseInt(br.readLine().trim());
			if (x > 0) {
				pQ.offer(x);
			} else if (x == 0) {
				if (pQ.isEmpty()) {
					System.out.println(0);
				} else {
					System.out.println(pQ.poll());
				}
			}
		}

	}
}