import java.io.*;
import java.util.*;

/*
 * 아이디어: 단순 구현, Map에 key,value로 담아두고 모두 처리 마친다음에 꺼내서 출력하려고 했다.
 * 하지만 그럴 필요 없이 그냥 key값만 식별 가능하게 넣어주고 바로 변환해서 출력하면 됐다.
 * 항상 코드를 구성할 때 가장 명료하고 논리적으로 구성했는가를 고민해보자. 불필요한 코드가 있지는 않는지 확인
 * 시간복잡도: O(N) N*5*10 => 상수항
 * 공간복잡도: O(N)
 */
public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());

		List<String>[] orders = new ArrayList[N];
		Map<Character, Integer> map = new HashMap<>();
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			orders[i] = new ArrayList<String>();
			while (st.hasMoreTokens()) {
				orders[i].add(st.nextToken());
			}
		}

		for (int i = 0; i < N; i++) {
			List<String> list = orders[i];
			boolean flag = false;

			// 1. 단어의 첫 번째 글자 검사
			for (int idx = 0; idx < list.size(); idx++) {
				String temp = orders[i].get(idx);
				char key = Character.toLowerCase(temp.charAt(0));
				if (!map.containsKey(key)) {
					map.put(key, i);
					list.set(idx, "[" + temp.charAt(0) + "]" + temp.substring(1));
					flag = true;
					break;
				}
			}

			// 2. 모든 글자 검사 후 추가
			// 첫 번째 글자 단축키로 지정했다면 끝
			if (!flag) {
				for (int idx = 0; idx < list.size(); idx++) {
					String temp = orders[i].get(idx);
					for (int k = 0; k < temp.length(); k++) {
						char key = temp.charAt(k);
						if (!map.containsKey(Character.toLowerCase(key))) {
							map.put(Character.toLowerCase(key), i);
							list.set(idx, temp.substring(0,k) + "[" + key + "]" + temp.substring(k+1));
							flag = true;
							break;
						}
					}

					// 이미 찾으면 종료
					if (flag) {
						break;
					}
				}
			}
			System.out.println(String.join(" ", list));
		}

	}
}