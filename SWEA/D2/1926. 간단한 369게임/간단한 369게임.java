import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

/*
 * 2초, 256MB
 * O(N), O(1)
 * 글자가 포함되는지 확인해야하기 때문에 HashMap으로 숫자를 저장하고 나오면 cnt를 늘려서 박수 개수를 구한다.
 */

public class Solution {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim()); // 숫자 개수: 10 <= N <= 1,000
		HashMap<Character, Boolean> map = new HashMap<>();
		map.put('3', true);
		map.put('6', true);
		map.put('9', true);
		
		for(int i = 1; i < N+1; i++) {
			String toNum = String.valueOf(i);
			int cnt = 0;
			
			for(int j = 0; j < toNum.length(); j++) {
				char num = toNum.charAt(j);
				if(map.containsKey(num)) {
					cnt++;
				}
			}
			
			if(cnt > 0) {
				for(int j = 0; j < cnt; j++) {
					System.out.print("-");
				}
				System.out.print(" ");
			}else {
				System.out.printf("%d ", i);
			}
		}
		
	}
}