import java.io.*;
import java.util.*;

/*
 * 2초, 256MB
 * 아이디어: 부분수열의 숫자를 다 더해서 S가 되는 경우의 수를 구한다.
 * 시간복잡도: O(2^N) => 100만
 * 공간복잡도: O(N)
 */

public class Main {
	static int N, S;
	static int[] arr;
	static boolean[] selected;
	static int result;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		N = Integer.parseInt(st.nextToken());
		S = Integer.parseInt(st.nextToken());
		arr = new int[N];
		selected = new boolean[N];
		result = 0;
		
		st = new StringTokenizer(br.readLine().trim());
		for(int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		dfs(0, 0, 0);
		
		System.out.println(result);
		
	}

	private static void dfs(int idx, int sum, int cnt) {
		// 기저
		if(idx == N) {
			if(cnt != 0 && sum == S) {
				result++;
			}
			return; // 결과에 상관없이 항상 return해야 올바름.
		}
		
		
		// 유도
		selected[idx] = true;
		dfs(idx+1, sum + arr[idx], cnt + 1);
		selected[idx] = false;
		dfs(idx+1, sum, cnt);
		
	}
}