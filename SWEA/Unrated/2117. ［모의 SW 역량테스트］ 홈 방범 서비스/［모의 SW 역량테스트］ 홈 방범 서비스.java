import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int N, M;
	static int[][] board;
	static int maxHouseCnt;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());
		
		for(int tc = 1; tc < T+1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			N = Integer.parseInt(st.nextToken()); // 도시 크기: 5 <= N <= 20
			M = Integer.parseInt(st.nextToken()); // 하나의 집 비용: 1 <= M <= 10
			board = new int[N][N];
			maxHouseCnt = 1;
			
			for(int i = 0; i < N; i++) {
				st = new StringTokenizer(br.readLine().trim());
				for(int j = 0; j < N; j++) {
					board[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int k = 2;
			while(k <= 24) {
				boolean flag = false;
				int operatingCost = k * k + (k-1) * (k-1);
				
				// 검사
				for(int i = 0; i < N; i++) {
					for(int j = 0; j < N; j++) {
						int houseCnt = checkHouseCnt(i,j,k);
						if(M * houseCnt >= operatingCost) {
//							System.out.println("i, j, houseCnt: " + i + " " + j + " " + houseCnt);
							flag = true;
							maxHouseCnt = Math.max(maxHouseCnt, houseCnt);
						}
					}
				}
				
//				if(!flag) {
//					break;
//				}
				
				k++;
//				System.out.println("===== 루프 한번 끝 =====");
			}
			
			System.out.printf("#%d %d\n", tc, maxHouseCnt);
			
		}

	}

	static int checkHouseCnt(int x, int y, int k) {
		int cnt = 0;
		int length = 2 * k - 1;
		int mid = length / 2;

		for (int i = 0; i < mid; i++) {
			for (int j = mid - i; j <= mid + i; j++) {
				int nx = x - (k-1) + i;
				int ny = y - (k-1) + j;
				if (isIn(nx, ny) && board[nx][ny] == 1) {
					cnt++;
				}
			}
		}

		for (int i = 0; i < length; i++) {
			int nx = x;
			int ny = y - (k-1) + i;
			if (isIn(nx, ny) && board[nx][ny] == 1) {
				cnt++;
			}
		}

		for (int i = mid + 1; i < length; i++) {
			for (int j = mid - (length - i - 1); j <= mid + (length - i - 1); j++) {
				int nx = x - (k-1) + i;
				int ny = y - (k-1) + j;
				if (isIn(nx, ny) && board[nx][ny] == 1) {
					cnt++;
				}
			}
		}
//		System.out.println("cnt: " + cnt);
		
		return cnt;
	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < N && ny >= 0 && ny < N;
	}
}