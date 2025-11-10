import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine().trim());

		int[] arr = new int[N + 1];
		int[] DP = new int[N + 1];

		for (int i = 1; i < N + 1; i++) {
			int cur = Integer.parseInt(br.readLine().trim());
			arr[i] = cur;
		}

		int maxLen = 1;
		for (int i = 1; i < N + 1; i++) {
			DP[i] = 1;
			for (int j = i; j >= 0; j--) {
				if (arr[j] < arr[i]) {
					DP[i] = Math.max(DP[i], DP[j] + 1);
					maxLen = Math.max(maxLen, DP[i]);
				}
			}
		}
		
		System.out.println(N - maxLen);
	}
}