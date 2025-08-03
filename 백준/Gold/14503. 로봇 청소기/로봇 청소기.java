import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
	
	public static void printArr(int[][] arr) {
		for(int[] x : arr) {
			System.out.println(Arrays.toString(x));
		}
	}
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		st = new StringTokenizer(br.readLine());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		int[][] arr = new int[n][m];
		int result = 0;

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				arr[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		int[] dr = { -1, 0, 1, 0 };
		int[] dc = { 0, 1, 0, -1 };
		while (true) {

			// 칸이 0이면 청소한다.
			if (arr[r][c] == 0) {
				arr[r][c] = 2;
				result += 1;
			}

			// 주변 4칸 검사
			boolean isClean = true;
			for (int i = 0; i < 4; i++) {
				int nr = r + dr[i];
				int nc = c + dc[i];

				if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
					if (arr[nr][nc] == 0) {
						isClean = false;
					}
				}
			}

			// 한 칸 후진 or 작동 정지
			if (isClean == true) {
				int nr = r - dr[d];
				int nc = c - dc[d];
				if (nr >= 0 && nr < n && nc >= 0 && nc < m && arr[nr][nc] != 1) {
						r = nr;
						c = nc;
						continue;
				}else if(arr[nr][nc] == 1){
					break;
				}
			} else {
				// 반시계로 90도 회전
				d = (d + 4 - 1) % 4;
				int nr = r + dr[d];
				int nc = c + dc[d];
				if(nr >= 0 && nr < n && nc >= 0 && nc < m) {
					if(arr[nr][nc] == 0) {
						r = nr;
						c = nc;
					}
				}
			}
			
//			printArr(arr);
//			System.out.println("-----------------------");
		}

		System.out.println(result);
	}
}
