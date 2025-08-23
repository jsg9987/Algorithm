import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Solution {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine().trim());
		
		for(int tc = 1; tc < T+1; tc++) {
			int N = Integer.parseInt(br.readLine().trim());
			boolean[] checkNum = new boolean[10];
			int checkCnt = 0;
			int result = N;
			int k = 2;
			
			String num = String.valueOf(N);
			for(int i = 0; i < num.length(); i++) {
				for(int j = 0; j < checkNum.length; j++) { 
					if(!checkNum[j] && (char)(j + '0') == num.charAt(i)) { // 아직 해당 숫자가 없고 해당 숫자가 나왔을 때
						checkCnt++;
						checkNum[j] = true;
					}
				}
			}
			
			if(checkCnt == 10) {
				System.out.printf("#%d %d\n", tc, N);
				continue;
			}
			
			
			while(checkCnt != 10) {
				result = (k++) * N;
				num = String.valueOf(result);
				for(int i = 0; i < num.length(); i++) {
					for(int j = 0; j < checkNum.length; j++) {
						if(!checkNum[j] && (char)(j + '0')== num.charAt(i) ) {
							checkCnt++;
							checkNum[j] = true;
						}
					}
				}
			}
			
			System.out.printf("#%d %d\n", tc, result);
		}
	}
}