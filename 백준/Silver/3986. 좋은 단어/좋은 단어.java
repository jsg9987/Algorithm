import java.io.*;
import java.util.*;

// 아이디어: 교차하지 않으려면 스택 두개를 사용해서 붙어서 나오는 알파벳쌍은 지우되, ABAB와 같이 알파벳쌍 사이에 다른 알파벳이 존재하면 무조건 실패
// 		   스택 b가 비었다면 교차하는 쌍이 존재하지 X
// 시간복잡도: O(N * 문자열 길이) => O(100 * 100,000), 그러나 모든 문자열의 길이 합은 1,000,000이므로 O(1,000,000)
// 공간복잡도: O(문자열 길이) => O(100,000)
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine().trim()); // N: 단어의 수(1 <= N <= 100)
		int result = 0;
		
		for(int i = 0; i < N; i++) {
			Deque<Character> a = new ArrayDeque<>();
			Deque<Character> b = new ArrayDeque<>();
			
			String input = br.readLine().trim();
			for(int j = 0; j < input.length(); j++) {
				a.offer(input.charAt(j));
			}
			
			while(!a.isEmpty()) {
				char cur = a.pollLast();
				
				// 비어있거나 서로 다른 알파벳이면 b에 삽입
				if(b.isEmpty() || b.peekLast() != cur) {
					b.offer(cur);
				} else if(b.peekLast() == cur) {
					b.pollLast();
				}
			}
			
			if(b.isEmpty()) result++;
		}
		
		bw.write(String.valueOf(result));
		bw.flush();
		bw.close();
		br.close();
	}
}