import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.IntStream;

/*
 * 1초, 256MB
 * M번동안 바구니를 역순으로 만들려고 한다. 역순으로 만들 범위를 정하고, 그 범위 내의 바구니를 역순으로
 * O(N*M), O(N)
 */

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int N = Integer.parseInt(st.nextToken()); // 바구니의 개수: 1 <= N <= 100
		int M = Integer.parseInt(st.nextToken()); // 역순으로 만드는 횟수: 1 <= M <= 100

		int[] arr = new int[N];
		for (int i = 0; i < N; i++) {
			arr[i] = i + 1;
		}
		

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int from = Integer.parseInt(st.nextToken()) - 1;
			int to = Integer.parseInt(st.nextToken()) - 1;

			int[] copy = Arrays.copyOfRange(arr, from, to+1);
			
			for(int j = 0; j <= to - from; j++) {
				arr[from + j] = copy[to - from - j];
			}
		}
		
		for(int e : arr) {
			System.out.printf("%d ", e);
		}
	}
}