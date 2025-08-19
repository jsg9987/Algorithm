import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * int형 자연수를 비트마스킹을 통해 비트 비교
 */
public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());
		
		for(int tc = 1; tc < T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int N = Integer.parseInt(st.nextToken());
			int M = Integer.parseInt(st.nextToken());
			
			boolean flag = true;
			for(int i = 0; i < N; i++) {
				if((M & (1 << i)) == 0) {
					flag = false;
					break;
				}
			}
			if(!flag) {
				System.out.printf("#%d OFF\n", tc);
			}else {
				System.out.printf("#%d ON\n", tc);
			}
			
		}
		
	}
}