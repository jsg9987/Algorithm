import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Queue;
import java.util.StringTokenizer;

public class Solution {
	static ArrayList<String> li;

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringBuilder sb = new StringBuilder();
		int T = 10;

		for (int tc = 1; tc < T + 1; tc++) {
			int N = Integer.parseInt(br.readLine().trim());
			li = new ArrayList<>();
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			sb.append("#").append(tc).append(" ");

			for (int i = 0; i < N; i++) {
				li.add(st.nextToken());
			}

			int orderCnt = Integer.parseInt(br.readLine().trim());

			st = new StringTokenizer(br.readLine().trim());
			for (int i = 0; i < orderCnt; i++) {
				String operate = st.nextToken();

				switch (operate) {
				case "I":
					int x = Integer.parseInt(st.nextToken()); // 앞부터 x번째에
					int y = Integer.parseInt(st.nextToken()); // y개
					String[] toInsert = new String[y];
					for (int j = 0; j < y; j++) {
						toInsert[j] = st.nextToken();
					}

					ArrayList<String> get = new ArrayList<>(Arrays.asList(toInsert));
					insert(x, y, get);
					break;
				case "D":
					int x1 = Integer.parseInt(st.nextToken()); // 앞부터 x번째에
					int y1 = Integer.parseInt(st.nextToken()); // y개 삭제
					delete(x1, y1);
					break;
				case "A":
					int y2 = Integer.parseInt(st.nextToken());
					ArrayList<String> get2 = new ArrayList<>();
					for(int j = 0; j < y2; j++) {
						get2.add(st.nextToken());
					}
					add(y2, get2);
				}
			}
			
			for(int i = 0; i < 10; i++) {
				sb.append(li.get(i));
				sb.append(" ");
			}
			sb.append("\n");
		}
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}

	static void insert(int x, int y, ArrayList<String> get) {
		for (int i = y - 1; i >= 0; i--) {
			li.add(x, get.get(i));
		}
	}

	static void delete(int x, int y) {
		for (int i = 0; i < y; i++) {
			li.remove(x);
		}
	}
	
	static void add(int y, ArrayList<String> get2) {
		li.addAll(get2);
	}
}