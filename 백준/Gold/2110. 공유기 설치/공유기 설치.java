import java.io.*;
import java.util.*;

/*
 * 아이디어: 전체 집 / 공유기 수로 나누어 떨어진 정수만큼 거리를 사용하는 그리디로 접근했음.
 * 안됨. 
 */

public class Main {
	static int N;
	static int[] arr;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		N = Integer.parseInt(st.nextToken()); // 집 개수: 1 <= N <= 200_000
		int C = Integer.parseInt(st.nextToken()); // 공유기 개수: 1 <= C <= 1_000_000_000
		int lo = 0;
		int hi = 0;
		arr = new int[N];
		
		for (int i = 0; i < N; i++) {
			int input = Integer.parseInt(br.readLine().trim());
			arr[i] = input;
		}
		
		Arrays.sort(arr);
		
		lo = 1;
		hi = arr[N-1] - arr[0] + 1; 
		
		while (lo < hi) {
			
			int mid = (hi + lo) / 2;
			
			if(verifyDist(mid) < C) {
				hi = mid;
			}else {
				lo = mid+1;
			}
//			System.out.println(lo + " , " + hi);
		}
		
		bw.write(String.valueOf(lo - 1));
		bw.flush();
		bw.close();
		br.close();
	}

	private static int verifyDist(int dist) {
		
		int tempCnt = 1;
		int preValue = arr[0];
		for(int i = 1; i < N; i++) {
			if(arr[i] >= preValue + dist) {
				preValue = arr[i];
				tempCnt++;
			}
		}
		
		return tempCnt;
	}
}