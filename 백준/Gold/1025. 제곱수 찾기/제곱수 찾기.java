import java.io.*;
import java.util.*;

/*
 * 아이디어: 8방향으로 숫자를 선택해 문자열을 만들고 완전제곱수인지 체크
 * 유형: 완탐
 * 시간복잡도: O(10^5 * 4) => O(N^5)
 * 공간복잡도: O(NM)
 * 
 * 복기
 * 완탐이란걸 알았지만 완벽하게 구현하긴 빡셌다. 
 * 놓친 부분: 현재 문자열이 완성된 후에 검증하는 로직이였는데, 완성되지 않더라도 등차수열로 만든 문자열임이 틀림없다.
 * 따라서 문자열이 완성되고 완전제곱수인지 검사하는게 아니라, 문자열이 만들어질 때마다 검증해서 갱신해야한다!
 * 메모리: 18452kb 시간: 128ms
 * 
 * 개선사항 -> c,r_diff를 -(N-1) <= <= (N-1)로 둔다면 하나의 for문안에서 모두 확인할 수 있다.
 */
public class Main {
	static int maxSqrt;
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int[][] board = new int[N][M];
		maxSqrt = -1;
		
		for(int i = 0; i < N; i++) {
			String input = br.readLine().trim();
			for(int j = 0; j < M; j++) {
				board[i][j] = input.charAt(j) - '0';
			}
		}
		
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < M; j++) {
				checkMaxSqrt(board[i][j]);
				for(int r_diff = -(N-1); r_diff < N; r_diff++) {
					for(int c_diff = -(M-1); c_diff < M; c_diff++) {
						if(r_diff == 0 && c_diff == 0) continue;
						// 문자열 만들기
						int x = i;
						int y = j;
						String temp = "";
						
//						System.out.println("문자만들기 시작");
						while(x>= 0 && x < N && y >= 0 && y < M) {
							temp += board[x][y];
//							System.out.println("무한루프  " + temp);
							
							checkMaxSqrt(Integer.parseInt(temp));
							x += r_diff;
							y += c_diff;
//							System.out.println("x, y = " + x + " " + y);
						}
//						System.out.println("문자만들기 끝");
						// 확인
//						System.out.println("현재 최대값: " + maxSqrt);
					}
				}
			}
		}
		
//		if(Math.sqrt(49) == Math.floor(Math.sqrt(49))) {
//			System.out.println(true );
//		}
		
		System.out.println(maxSqrt);
	}
	
	private static void checkMaxSqrt(int num) {
		double sqrt = Math.sqrt(num);
		if(Math.floor(sqrt) == sqrt) {
			maxSqrt = Math.max(num, maxSqrt);
		}
	}
}