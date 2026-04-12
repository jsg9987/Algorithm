import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import javax.swing.InputMap;

public class Main {
	static int N, M;
	static int[] parents;
	static int result;

	public static void main(String[] args) throws NumberFormatException, IOException {
		// --------------솔루션 코드를 작성하세요.---------------------------
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		N = Integer.parseInt(st.nextToken()); // 유적지 개수 N (3 <= n <= 500,000)
		M = Integer.parseInt(st.nextToken()); // 설치될 통로 수 M (3 <= M <= 1,000,000)
		parents = new int[N]; // 노드 개수만큼 부모배열
		result = 0;
		make();
		boolean flag = false;

		// m줄동안 통로 연결
		for (int time = 0; time < M; time++) {
			st = new StringTokenizer(br.readLine().trim());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			result++;
			if(!union(a,b)) { 
				flag = true;
				break;
			}
		}

		// m개의 통로 다 설치하면 result가 m과 동일
		if(result == M && !flag) result = 0;
		
		System.out.println(result);
	}

	static void make() {
		for (int i = 0; i < N; i++) {
			parents[i] = i;
		}
	}

	static int findRoot(int a) {
		if (parents[a] == a)
			return a;
		return parents[a] = findRoot(parents[a]); // 최적화
	}

	static boolean union(int a, int b) {
		int aRoot = findRoot(a);
		int bRoot = findRoot(b);

		if (aRoot == bRoot)
			return false;

		if (aRoot > bRoot) {
			parents[bRoot] = aRoot;
			return true;
		}else{
			parents[aRoot] = bRoot;
			return true;
		}
	}

}
