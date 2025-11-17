import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		Scanner scan = new Scanner(System.in);
		int T = Integer.parseInt(br.readLine().trim());

		for (int tc = 0; tc < T; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int N = Integer.parseInt(st.nextToken()); // 팀의 개수: 3 <= N <= 100
			int K = Integer.parseInt(st.nextToken()); // 문제의 개수: 3 <= K <= 100
			int teamId = Integer.parseInt(st.nextToken()) - 1; // 우리팀 번호: 1 <= teamId <= N
			int M = Integer.parseInt(st.nextToken()); // 로그 엔트리 개수: 3 <= M <= 10_000

			int[] totalSum = new int[N]; // 각 팀의 총점
			int[][] problemScore = new int[N][K]; // 각 팀의 문제별 점수
			int[] lastSubmit = new int[N]; // 각 팀의 마지막 제출 시간
			int[] submitCnt = new int[N]; // 각 팀의 제출 횟수

			for (int i = 0; i < M; i++) {
				st = new StringTokenizer(br.readLine().trim());
				int id = Integer.parseInt(st.nextToken()) - 1; // 현재 팀번호
				int problemNum = Integer.parseInt(st.nextToken()) - 1; // 문제 번호
				int score = Integer.parseInt(st.nextToken()); // 획득 점수

				// 점수가 갱신됐다면?
				if (score > problemScore[id][problemNum]) {
					totalSum[id] -=  problemScore[id][problemNum];
					totalSum[id] += score;
					problemScore[id][problemNum] = score;
				}
				
				// 마지막 제출시간 갱신
				lastSubmit[id] = i;
				
				// 각 팀 제출 횟수 갱신
				submitCnt[id]++;
			}

			int result = 1;
			for(int i = 0; i < N; i++) {
				if(i == teamId) continue;
				
				if(totalSum[i] > totalSum[teamId]) {
					result++;
				}else if(totalSum[i] == totalSum[teamId] && submitCnt[i] < submitCnt[teamId]) {
					result++;
				}else if(totalSum[i] == totalSum[teamId] && submitCnt[i] == submitCnt[teamId] && lastSubmit[i] < lastSubmit[teamId]) {
					result++;
				}
			}
			
			System.out.println(result);
		}

	}
}
