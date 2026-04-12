import java.io.*;
import java.util.*;

public class Main {
	public static void main(String args[]) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine().trim());
		
		for(int tc = 1; tc < T+1; tc++) {
			int N = Integer.parseInt(br.readLine().trim());
			long max = 0;
			int cnt = 0;
			long cost = 0;
			long result = 0;
			int[] arr = new int[N];
			
			StringTokenizer st= new StringTokenizer(br.readLine().trim());
			for(int i = 0; i < N; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
			}
			
			for(int i = N-1; i >= 0; i--) {
				int cur = arr[i];
				if(cur > max) {
					// 지금까지 산 주식을 판다.
					result += max * cnt - cost;
					cnt = 0;
					cost = 0;
					
					// 새로운 max 갱신
					max = cur;
				}else if(cur < max){
					cost += cur;
					cnt++;
				}
			}
			result += max * cnt - cost;
			
			bw.write(String.valueOf(result));
			bw.write("\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}