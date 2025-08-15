import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

/*
 핵심 아이디어: 왼쪽 시작 인덱스부터 dfs로 우뚝 선 산 개수를 추가하려함. 근데 재귀가 최대 50000번까지 깊어지는데 가지치기할 방법이 안보였음.
 다른 방법이 생각나지 않아 dfs로 구현하다 재귀 스택오버플로우가 뜸. 시간복잡도 O(N^2) -> 25억.. 불가능
 복기: 투포인터를 사용(여기서도 O(N^2)주의)
 아이디어: 봉우리가 되는 위치를 찾아 좌우 길이를 구하고 둘을 곱하면 해당 봉우리에서 가능한 가지 수가 나온다.
 시간복잡도: O(N) 공간복잡도: O(N)
 입력 Scanner 이슈..
 */
public class Solution {
	static int N;
	static int[] arr;
	static long result; // 가지 수가 int범위 넘어갈 수 있으니 long 사용

	public static void main(String[] args) throws IOException {
//		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc < T + 1; tc++) {
			N = sc.nextInt();
			arr = new int[N];
			result = 0;

			for (int i = 0; i < N; i++) {
				arr[i] = sc.nextInt();
			}

			// 투포인터
			for (int i = 1; i < N - 1; i++) {
				// 산 정상 조건
				if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
					int left = 0, right = 0; // 왼쪽, 오른쪽 길이

					// 왼쪽 길이 구하기
					int l = i - 1;
					while (l >= 0 && arr[l] < arr[l + 1]) {
						left++;
						l--;
					}

					// 오른쪽 길이 구하기
					int r = i + 1;
					while (r < N && arr[r] < arr[r - 1]) {
						right++;
						r++;
					}

					result += (long) left * right;
				}
			}
			System.out.printf("#%d %d\n", tc, result);
		}
		sc.close();
	}

//	static void dfs(int idx, int cnt, boolean flag) {
//		// 범위 넘어가면 end
//		if(idx >= N) return;
//		
//		// 기저 조건: preIdx보다 작은 값이 나왔을 때
//		if (cnt >= 2 && idx > 0 && idx < N && arr[idx] < arr[idx - 1]) {
//			if (cnt >= 3) {
//				result++;
//				dfs(idx + 1, cnt + 1, true);
//			}
//			return;
//		} 
//		
//		if(flag) return; // 우뚝 선 산에서 다시 위로 꺾일 때
//
//		dfs(idx + 1, cnt + 1, false);
//	}
}