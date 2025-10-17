import java.io.*;
import java.util.*;

public class Main {
	static int N;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		N = Integer.parseInt(br.readLine().trim()); // 스위치 개수: 1 <= N <= 100
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int[] switches = new int[N];
		for (int i = 0; i < N; i++) {
			switches[i] = Integer.parseInt(st.nextToken());
		}

		int repeat = Integer.parseInt(br.readLine().trim());

		for (int i = 0; i < repeat; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int gender = Integer.parseInt(st.nextToken()); // 성별: 1:남 2:여
			int num = Integer.parseInt(st.nextToken()); // 번호

			if (gender == 1) {
				for (int j = num-1; j < N; j += num) {
					switches[j] = switches[j] ^ 1;
				}
			} else if (gender == 2) {
				int idx = num-1;
				switches[idx] = switches[idx] ^ 1;
				int left = idx - 1;
				int right = idx + 1;
				while (isIn(left, right) && switches[left] == switches[right]) {
					switches[left] = switches[left] ^ 1;
					switches[right] = switches[right] ^ 1;
					left--;
					right++;
				}
			}
//			System.out.println(Arrays.toString(switches));
		}

		for (int i = 0; i < N; i++) {
			sb.append(switches[i]).append(" ");
			if((i+1) % 20 == 0) sb.append("\n");
		}

		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();

	}

	private static boolean isIn(int left, int right) {
		return left >= 0 && right < N;
	}
}