import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine().trim());
		int[] input = new int[N]; // 첫번째 스위치 안누름.
		int[] answer = new int[N];
		int[] input2 = new int[N]; // 첫번째 스위치 누름.
		String data = br.readLine().trim();
		for (int i = 0; i < N; i++) {
			input[i] = data.charAt(i) - '0';
			input2[i] = data.charAt(i) - '0';
		}

		input2[0] ^= 1;
		if (N >= 2) {
			input2[1] ^= 1;
		}
		String ans = br.readLine().trim();

		for (int i = 0; i < N; i++) {
			answer[i] = ans.charAt(i) - '0';
		}

		int cnt1 = 0;
		int cnt2 = 1;
		int result = -1;
		for (int i = 1; i < N; i++) {
			// input의 i-1의 자리가 answer와 다르다면 i번째 스위치를 누름.
			if (i != N - 1 && input[i - 1] != answer[i - 1]) {
				input[i - 1] ^= 1;
				input[i] ^= 1;
				input[i + 1] ^= 1;
				cnt1++;
			} else if (i == N - 1 && input[i - 1] != answer[i - 1]) {
				input[i - 1] ^= 1;
				input[i] ^= 1;
				cnt1++;
			}

			// input2의 i-1의 자리가 answer와 다르다면 i번째 스위치를 누름.
			if (i != N - 1 && input2[i - 1] != answer[i - 1]) {
				input2[i - 1] ^= 1;
				input2[i] ^= 1;
				input2[i + 1] ^= 1;
				cnt2++;
			} else if (i == N - 1 && input2[i - 1] != answer[i - 1]) {
				input2[i - 1] ^= 1;
				input2[i] ^= 1;
				cnt2++;
			}
		}

		StringBuilder sb = new StringBuilder();
		for (int i : input) {
			sb.append(i);
		}
		String output1 = sb.toString();
		sb = new StringBuilder();

		for (int i : input2) {
			sb.append(i);
		}
		String output2 = sb.toString();

		if (ans.equals(output1) && !ans.equals(output2)) {
			result = cnt1;
		} else if (!ans.equals(output1) && ans.equals(output2)) {
			result = cnt2;
		} else if (ans.equals(output1) && ans.equals(output2)) {
			result = Math.min(cnt1, cnt2);
		}

		bw.write(String.valueOf(result));
		bw.flush();
		bw.close();
		br.close();
	}
}