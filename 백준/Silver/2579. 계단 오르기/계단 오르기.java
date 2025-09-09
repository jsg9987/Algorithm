import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		int[] stairs = new int[N + 1];
		for (int i = 1; i < N + 1; i++) {
			stairs[i] = Integer.parseInt(br.readLine().trim());
		}
		int[] DP = new int[N + 1];
		DP[0] = 0;
		
		if (N > 0)
			DP[1] = stairs[1];
		if (N > 1)
			DP[2] = stairs[1] + stairs[2];
		if (N > 2)
			DP[3] = Math.max(stairs[1] + stairs[3], stairs[2] + stairs[3]);

		for (int i = 4; i < N + 1; i++) {
			DP[i] = Math.max(DP[i - 2] + stairs[i], DP[i - 3] + stairs[i - 1] + stairs[i]);
		}

		System.out.println(DP[N]);

	}
}