import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine().trim()); // 전체 용액 수: 2 <= N <= 10_000
		int[] arr = new int[N];
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		for(int i = 0; i < N; i++) {
			int cur = Integer.parseInt(st.nextToken());
			arr[i] = cur;
		}
		
		// 투포인터로 최소 해 찾기
		int left = 0;
		int right = N-1;
		int minLeft = 0;
		int minRight = N-1;
		int minSum = Integer.MAX_VALUE;
		
		while(left < right) {
			
			int tempSum = arr[left] + arr[right];
			if(Math.abs(tempSum) < minSum) { // 절대값화
				minSum = Math.abs(tempSum);
				minLeft = left;
				minRight = right;
			}
			
			// 합이 음수인 경우, 양수인 경우
			if(tempSum < 0) {
				left++;
			}else if(tempSum > 0) {
				right--;
			}else if(tempSum == 0) {
				break;
			}
		}
		
		bw.write(String.valueOf(arr[minLeft]) + " ");
		bw.write(String.valueOf(arr[minRight])); 
		bw.flush();
		bw.close();
		br.close();
	}
}