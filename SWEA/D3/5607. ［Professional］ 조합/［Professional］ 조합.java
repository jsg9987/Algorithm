import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static final int MOD = 1234567891;
	static final int MAX = 1000001;
	static int N,R; 
	static long[] DP;
	
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());
		DP = new long[MAX];
		DP[1] = 1;
		
		for(int i = 2; i < MAX; i++) {
			DP[i] = (DP[i-1] * i) % MOD;
		}
		
		for(int tc = 1; tc < T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			N = Integer.parseInt(st.nextToken());
			R = Integer.parseInt(st.nextToken());
			
			// 분모
			long bottom = (DP[N-R] * DP[R]) % MOD;
			
			long b_inverse = power(bottom, MOD - 2);
			long answer = (DP[N] * b_inverse) % MOD;
			
			System.out.printf("#%d %d\n", tc, answer);
		}
	}
	
	// 거듭제곱을 구하는 함수(분할 정복 이용)
	public static long power(long base, long exp) {
		if(exp == 0) {
			return 1;
		}else if(exp == 1) {
			return base;
		}if(exp % 2 == 0) {
			long temp = power(base, exp /2);
			return (temp * temp) % MOD;
		}
		long temp = power(base, exp-1);
		return (temp * base) % MOD;
	}
	
		
		
}