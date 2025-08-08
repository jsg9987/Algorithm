import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int[] sumArr;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int[] arr = new int[N + 1];
		sumArr = new int[N + 1];
		for (int i = 1; i < N + 1; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		for (int i = 1; i < N + 1; i++) {
			sumArr[i] = sumArr[i - 1] + arr[i];
		}

		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());
			System.out.println(prefixSum(x,y));
		}

	}

	static int prefixSum(int x, int y) {
		return sumArr[y] - sumArr[x - 1];
	}

}