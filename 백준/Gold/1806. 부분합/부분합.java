import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		int N = Integer.parseInt(st.nextToken()); // 수열 길이: 10 <= N <= 100_000
		int S = Integer.parseInt(st.nextToken()); // 부분합 S: 0 < S <= 100_000_000
		int[] arr = new int[N+1];
		int[] Sum = new int[N+1];

		st = new StringTokenizer(br.readLine().trim());
		for (int i = 1; i < N+1; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 1; i < N+1; i++) {
			Sum[i] = Sum[i - 1] + arr[i];
		}

//		System.out.println(Arrays.toString(Sum));

		int left = 0; 
		int right = 1;
		int INF = 1_000_000_000;
		int result = INF;
		while(left < N+1 && right < N+1) {
			int sum = Sum[right] - Sum[left];
//			System.out.println(left + " " + right);
//			System.out.println("sum" + sum);
			if(sum < S) {
				right++;
			}else if(sum >= S) {
				result = Math.min(result, right - left);
				left++;
			}
		}
		
		result = (result == INF) ? 0: result;
		System.out.println(result);
	}
}