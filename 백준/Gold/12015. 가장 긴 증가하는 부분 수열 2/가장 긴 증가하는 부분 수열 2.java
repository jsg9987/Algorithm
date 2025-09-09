import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		int[] arr = new int[N];
		int[] C = new int[N];
		Arrays.fill(C, Integer.MAX_VALUE);
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		int result = 0;
		
		for(int i = 0; i < N; i++) { // O(N)
			int idx = Arrays.binarySearch(C, arr[i]); // O(logN)
			if(idx < 0) {
				C[-(idx + 1)] = arr[i];
			}else {
				C[idx] = arr[i];
			}
		}
		
		for(int i = N-1; i >= 0; i--) {
			if(C[i] != Integer.MAX_VALUE) {
				result = i + 1;
				break;
			}
		}
		
		System.out.println(result);
		
	}
}