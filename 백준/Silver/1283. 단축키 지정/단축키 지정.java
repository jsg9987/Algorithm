import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine().trim());

        List<String>[] orders = new ArrayList[N];
        Set<Character> used = new HashSet<>();

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            orders[i] = new ArrayList<>();
            while (st.hasMoreTokens()) {
                orders[i].add(st.nextToken());
            }
        }

        for (int i = 0; i < N; i++) {
            List<String> list = orders[i];
            boolean flag = false;

            // 1. 각 단어의 첫 글자 검사
            for (int idx = 0; idx < list.size(); idx++) {
                String temp = list.get(idx);
                char key = Character.toLowerCase(temp.charAt(0));
                if (!used.contains(key)) {
                    used.add(key);
                    list.set(idx, "[" + temp.charAt(0) + "]" + temp.substring(1));
                    flag = true;
                    break;
                }
            }

            // 2. 모든 글자 검사
            if (!flag) {
                outer:
                for (int idx = 0; idx < list.size(); idx++) {
                    String temp = list.get(idx);
                    for (int k = 0; k < temp.length(); k++) { // 0부터
                        char key = Character.toLowerCase(temp.charAt(k));
                        if (!used.contains(key)) {
                            used.add(key);
                            list.set(idx, temp.substring(0, k) + "[" + temp.charAt(k) + "]" + temp.substring(k + 1));
                            break outer;
                        }
                    }
                }
            }

            System.out.println(String.join(" ", list));
        }
    }
}
