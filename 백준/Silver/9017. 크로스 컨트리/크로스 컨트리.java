import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine().trim());

		for (int i = 0; i < T; i++) {
			// 1. 입력받으면서 각 팀의 인원수와 max_team_cnt를 확인한다.
			// 2. result 점수 배열에 유효하지 않은 팀은 Max값으로 초기화 후 각 팀의 점수를 계산한다.
			// 3. 가장 작은 점수의 팀을 출력
			int N = Integer.parseInt(br.readLine().trim());
			int maxTeamCnt = 200;
			int maxTeamNum = 0;
			int[] memberCnt = new int[maxTeamCnt];
			int[] teamNum = new int[N];
			int INF = 1_000_000_000;

			StringTokenizer st = new StringTokenizer(br.readLine());
			for (int j = 0; j < N; j++) {
				int cur = Integer.parseInt(st.nextToken());
				teamNum[j] = cur;
				if (cur > maxTeamNum) {
					maxTeamNum = cur;
				}
				memberCnt[cur - 1]++;
			}

			boolean[] isValidTeam = new boolean[maxTeamNum];
			for (int j = 0; j < maxTeamNum; j++) {
				if (memberCnt[j] == 6) {
					isValidTeam[j] = true;
				}
			}

			int[] scoreArr = new int[maxTeamNum];
			for (int j = 0; j < maxTeamNum; j++) {
				if (!isValidTeam[j]) {
					scoreArr[j] = INF;
				}
			}

			int score = 1;
			int[] cnt4th = new int[maxTeamNum];
			int[] score5th = new int[maxTeamNum];
			for (int j = 0; j < N; j++) {
				if (isValidTeam[teamNum[j] - 1]) {
					if (cnt4th[teamNum[j] - 1] < 4) {
						scoreArr[teamNum[j] - 1] += score;
						cnt4th[teamNum[j] - 1]++;
					} else if(cnt4th[teamNum[j] - 1] == 4){
						score5th[teamNum[j] - 1] = score;
						cnt4th[teamNum[j] - 1]++;
					}
					score++;
				}
			}

			int minScore = INF;
			int resultIdx = 0;
			for (int j = 0; j < maxTeamNum; j++) {
				if (scoreArr[j] < minScore) {
					minScore = scoreArr[j];
					resultIdx = j;
				} else if(scoreArr[j] == minScore) {
					if(score5th[resultIdx] > score5th[j]) {
						resultIdx = j; 
					}
				}
			}

			bw.write(String.valueOf(resultIdx + 1) + "\n");
		}
		bw.flush();
		bw.close();
		br.close();
	}
}