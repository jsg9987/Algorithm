import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int N = Integer.parseInt(st.nextToken()); // 전체개수: 1<= N <= P
		int curScore = Integer.parseInt(st.nextToken());
		int P = Integer.parseInt(st.nextToken()); // 랭킹리스트 개수: 10 <= P <= 50
		List<Integer> rank = new ArrayList<>();

		if (N != 0) {
			st = new StringTokenizer(br.readLine().trim());
		}

		for (int i = 0; i < N; i++) {
			int cur = Integer.parseInt(st.nextToken());
			rank.add(cur);
		}

		int insertIdx = -1;
		for(int i = 0; i < P; i++) {
			if(i >= N || curScore > rank.get(i)) {
				rank.add(i, curScore);
				insertIdx = i;
				break;
			}
		}
		
		if(insertIdx != -1) {
			insertIdx = rank.indexOf(curScore) + 1;
		}
		
		System.out.println(insertIdx);

	}
}