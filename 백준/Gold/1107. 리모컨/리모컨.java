import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static boolean[] cantUse;
	static int N, M;
	static int minDiff;
	static int start;
	static int N_length;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine().trim()); // 이동하려고 하는 채널번호 0 <= N <= 500,000
		M = Integer.parseInt(br.readLine().trim()); // 고장난 버튼 개수 0<= M <= 10 -> 숫자버튼만
		N_length = String.valueOf(N).length();
		cantUse = new boolean[10];
		start = 100;
		minDiff = Math.abs(N - start);
		
		if (M != 0) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			for (int i = 0; i < M; i++) {
				int idx = Integer.parseInt(st.nextToken());
				cantUse[idx] = true;
			}
		}


		getStartNum("");

		int result = (N == 100) ? 0 : String.valueOf(start).length();
//		System.out.println("start: " + start);
//		System.out.println("minDiff: " + minDiff);
//		System.out.println("result: " + result);
		System.out.println(minDiff);

	}

	// 중복순열로 가장 가까운 숫자를 먼저 찾는다.
	private static void getStartNum(String tempN) {
//		System.out.println(tempN);
		// 기저 조건: N의 길이만큼 다 뽑았다면 비교, 최소 Diff 갱신
		if (!tempN.isEmpty()) {
			int channel = Integer.parseInt(tempN);
			
			int currentCnt = tempN.length() + Math.abs(channel - N); 
			
			// 최솟값 갱신
			minDiff = Math.min(minDiff, currentCnt);
			
			// 더 길어지면 종료
			if (tempN.length() == N_length+1) {
				return;
			}
		}

		// 유도 파트
		for (int i = 0; i < 10; i++) {
			if (cantUse[i]) {
				continue;
			}
			getStartNum(new String(tempN + i));
		}

		return;
	}
}