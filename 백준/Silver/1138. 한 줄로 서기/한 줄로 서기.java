import java.io.*;
import java.util.*;

/*
 * 20:23 ~ 20:47
 * 2초, 128MB
 * 아이디어: 제일 큰 수부터 List의 맨 앞에 넣고, 차례대로 그 다음 숫자가 올 자리를 판단해서 사이에 끼워넣는다.
 * 시간복잡도: O(N^2)
 * 공간복잡도: O(N)
 */
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim()); // 사람 수: 1 <= N <= 10
		int[] arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		List<Integer> line = new ArrayList<>();
		line.add(N);
		
		for(int i = N-2; i >= 0; i--) {
			int idx = arr[i];
			line.add(idx, i+1);
		}
		
		for(int e : line) {
			System.out.printf("%d ", e);
		}
	}
}
