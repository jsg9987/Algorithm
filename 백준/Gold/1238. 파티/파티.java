import java.io.*;
import java.util.*;

public class Main {
	static int INF = 100_000_000;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());

		int N = Integer.parseInt(st.nextToken()); // 학생 수: 1 <= N <= 1_000
		int M = Integer.parseInt(st.nextToken()); // 단방향 도로 개수: 1 <= M <= 10_000
		int X = Integer.parseInt(st.nextToken()) - 1; // 도착지점 X
		
		int[][] graph = new int[N][N];
		for(int i = 0; i < N; i++) {
			for(int j = 0; j < N; j++) {
				if(i == j) {
					graph[i][j] = 0;
				}else {
					graph[i][j] = INF;
				}
			}
		}
		
		for(int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine().trim());
			int start = Integer.parseInt(st.nextToken())-1; // 도로 시작점
			int end = Integer.parseInt(st.nextToken())-1; // 도로 끝점
			int time = Integer.parseInt(st.nextToken()); // 소요시간 
			
			graph[start][end] = time;
		}
		
		for(int k = 0; k < N; k++) {
			for(int i = 0; i < N; i++) {
				for(int j = 0; j < N; j++) {
					graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
				}
			}
		}
		
		int result = 0;
		for(int i = 0; i < N; i++) {
			int timeSum = graph[i][X] + graph[X][i];
			result = Math.max(result, timeSum);
		}
		
		bw.write(String.valueOf(result));
		bw.flush();
		bw.close();
		br.close();
	}
}