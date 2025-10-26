import java.io.*;
import java.util.*;

public class Main {
	static int MAX_PRICE = 100_001;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		for (int tc = 0; tc < 3; tc++) {
			int N = Integer.parseInt(br.readLine().trim());
			boolean[][] DP = new boolean[N + 1][MAX_PRICE];
			DP[0][0] = true; // 0원은 항상 true
			int sum = 0;
			
			for (int i = 1; i < N+1; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine().trim());
				int coin = Integer.parseInt(st.nextToken());
				int cnt = Integer.parseInt(st.nextToken());
				sum += coin * cnt;

				// 그 전의 동전들을 사용한 결과에서 이번 동전들을 사용한 결과를 갱신
				for (int price = 0; price < MAX_PRICE; price++) {
					if (DP[i - 1][price] == true) {
						for (int j = 0; j < cnt+1; j++) {
							int new_price = price + coin * j;
							if (new_price < MAX_PRICE) {
								DP[i][new_price] = true;
							}
						}
					}
				}
			}
			
//			for(int i = 0; i < N+1; i++) {
//				System.out.println(Arrays.toString(DP[i]));
//			}
			
			if(sum % 2 == 0 && DP[N][sum / 2]) {
				bw.write(String.valueOf(1) + "\n");
			}else {
				bw.write(String.valueOf(0) + "\n");
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
}