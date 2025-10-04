import java.io.*;
import java.util.*;


/*
 * 10초, 512MB, 00:45 ~ 01:18
 * 땅 개수 N <= 200
 * 아이디어: 
 */
public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		
		for(int tc = 0; tc < N; tc++) {
			HashMap<String, Integer> map = new HashMap<>();
			HashSet<String> set = new HashSet<>();
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			int cnt = Integer.parseInt(st.nextToken());
			
			for(int i = 0; i < cnt; i++) {
				String cur = st.nextToken();
				set.add(cur);
				if(map.containsKey(cur)) {
					map.put(cur, map.get(cur) + 1);
				}else {
					map.put(cur, 1);
				}
			}
			
			boolean flag = false;
			for(String e : set) {
				if(map.get(e) > cnt / 2) {
					System.out.println(e);
					flag = true;
					break;
				}
			}
			
			if(!flag) {
				System.out.println("SYJKGW");
			}
		}
	}
}