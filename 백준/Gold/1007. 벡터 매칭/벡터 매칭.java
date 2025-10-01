import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static long totalX, totalY;
	static int[] xCoords;
	static int[] yCoords;
	static double minValue;
	static boolean[] selected;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 0; tc < T; tc++) {
			N = Integer.parseInt(br.readLine().trim());
			xCoords = new int[N];
			yCoords = new int[N];
			minValue = Double.MAX_VALUE;
			selected = new boolean[N];
            totalX = 0;
            totalY = 0;
			
			

			for (int i = 0; i < N; i++) {
				StringTokenizer st = new StringTokenizer(br.readLine().trim());
				xCoords[i] = Integer.parseInt(st.nextToken());
				yCoords[i] = Integer.parseInt(st.nextToken());
				totalX += xCoords[i];
				totalY += yCoords[i];
			}

			dfs(0, 0);
			
			System.out.println(minValue);
		}

	}

	private static void dfs(int start, int pairCnt) {

		// 종료 조건
		if(pairCnt == N/2) {
			
			long xSum = 0;
			long ySum = 0;
			
			for(int i = 0; i < N; i++) {
				if(selected[i]) {
					xSum += xCoords[i];
					ySum += yCoords[i];
				}
			}
			
			long arrivalXSum = totalX - xSum;
			long arrivalYSum = totalY - ySum;
			
			double result = Math.sqrt((arrivalXSum - xSum)* (arrivalXSum - xSum) + (arrivalYSum - ySum) * (arrivalYSum - ySum));
			
			minValue = Math.min(minValue, result);
		}

		// 유도
		for(int i = start; i < N; i++) {
			selected[i] = true;
			dfs(i+1, pairCnt + 1);
			
			selected[i] = false;
			
		}
	}
}