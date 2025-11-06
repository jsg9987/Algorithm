import java.io.*;
import java.util.*;

/*
 * 아이디어: 상한액이 1 ~ 10만까지 가능하기에 선형탐색하면 시간초과됨.
 * 상한액을 기준으로 파라메트릭 서치하면 O(NlogN) 시간 안에 계산 가능함.
 * 시간복잡도: O(NlogN)
 * 공간복잡도: O(N)
 * memory: 13848 time: 100
 */
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		int N = Integer.parseInt(br.readLine().trim()); // 지방의 수: 1 <= N <= 10_000
		int[] arr = new int[N];
		int maxValue = 0;
		int sum = 0;
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for (int i = 0; i < N; i++) {
			int temp = Integer.parseInt(st.nextToken());
			sum += temp;
			maxValue = Math.max(maxValue, temp);
			arr[i] = temp;
		}

		int maxAmount = Integer.parseInt(br.readLine().trim());
		boolean flag = false;
		if (maxAmount > sum) {
			flag = true;
		}

		int left = 1;
		int right = maxValue;

		if (!flag) {
			while (left <= right) {
				int mid = (left + right) / 2;
				int tempSum = 0;

				// 이번 상한액 적용해서 계산
				for (int i = 0; i < N; i++) {
					tempSum += Math.min(arr[i], mid);
				}

				// 상한액이 초과하면 right를 mid로 이동
				if (tempSum > maxAmount) {
					right = mid - 1;
				} else if (tempSum < maxAmount) {
					// 상한액이 충족되면 left 이동
					left = mid + 1;
					maxValue = mid;
				} else {
					maxValue = mid;
					break;
				}
			}
		}

		bw.write(String.valueOf(maxValue));
		bw.flush();
		bw.close();
		br.close();
	}
}
