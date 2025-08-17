// 14:53 ~ 
// tc: 30, 2 <= N <= 100, heightMax==120
// 최대 나무높이로 뺐을 때 1이 더 많은 경우, 2가 더 많은 경우, 같은 경우

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc < T + 1; tc++) {
			int N = Integer.parseInt(br.readLine());
			int[] arr = new int[N];
			int MAX = 0;
			int one = 0;
			int two = 0;
			int cnt = 0;
			StringTokenizer st = new StringTokenizer(br.readLine());

			for (int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				MAX = Math.max(MAX, arr[i]);
			}

			for (int i = 0; i < N; i++) {
				arr[i] = MAX - arr[i];
				one += arr[i] % 2;
				two += arr[i] / 2;
			}

			if (one > two) {
				cnt += two * 2;
				one -= two;
				two = 0;
				cnt += one * 2 - 1;
			} else if (two > one) {
				cnt += one * 2;
				two -= one;
				one = 0;
				int bundle = two / 3;
				cnt += bundle * 4;
				two -= bundle * 3;
				if (two == 1) {
					cnt += two * 2;
				} else if (two == 2) {
					cnt += 3;
				}
			} else {
				cnt += one * 2;
			}

			System.out.printf("#%d %d\n", tc, cnt);

		}

	}
}
