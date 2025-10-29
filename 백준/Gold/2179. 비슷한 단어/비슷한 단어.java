import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		// 문자열 개수: 1 <= N <= 20_000, 각 길이 <= 100
		int N = Integer.parseInt(br.readLine().trim());
		String[] words = new String[N];

		for (int i = 0; i < N; i++) {
			words[i] = br.readLine().trim();
		}

		int left = 0;
		int max_len = 0;
		Map<String, Integer> map = new HashMap<>();
		String init_S = words[left];
		String init_T = words[left+1];
		int result_left = 0;
		int result_right = 1;
		for (int i = 0; i < N; i++) {
			map.put(words[i], i);
		}

		Arrays.sort(words);

		while (left < N) {
			
			int right = left + 1;

			while(right < N) {
				String word1 = words[left];
				String word2 = words[right];
				int tempMax = 0;
				int length = Math.min(word1.length(), word2.length());
				
				for (int i = 0; i < length; i++) {
					if (!word1.equals(word2) && word1.charAt(i) == word2.charAt(i)) {
						tempMax++;
					} else {
						break;
					}
				}
				
				if (tempMax > max_len) {
					max_len = tempMax;
					result_left = left;
					result_right = right;
				}else if(max_len == tempMax) {
					int result_idx = Math.min(map.get(words[result_left]), map.get(words[result_right]));
					int temp_idx = Math.min(map.get(word1), map.get(word2));
					if(temp_idx < result_idx) {
						result_left = left;
						result_right = right;
					}
				}
				else if(max_len > tempMax) {
					break;
				}
				
				right++;
			}

			left++;
		}

		if (max_len > 0) {
			if (map.get(words[result_left]) < map.get(words[result_right])) {
				bw.write(words[result_left] + "\n");
				bw.write(words[result_right]);
			}else if(map.get(words[result_left]) > map.get(words[result_right])){
				bw.write(words[result_right] + "\n");
				bw.write(words[result_left]);
			}
		} else {
			bw.write(init_S + "\n");
			bw.write(init_T);
		}

		bw.flush();
		bw.close();
		br.close();
	}
}