import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashSet;

/*
 * HashSet을 사용해서 코드 간단하게
 */

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();
        
        int T = Integer.parseInt(br.readLine().trim());

        for (int tc = 1; tc <= T; tc++) {
            int N = Integer.parseInt(br.readLine().trim());
            HashSet<Integer> set = new HashSet<>();
            int result = N;
            int k = 2;

            // 10개 찾을 때까지
            while (set.size() != 10) {
                String num = String.valueOf(result);
                for (int i = 0; i < num.length(); i++) {
                    set.add(num.charAt(i) - '0'); // 숫자 하나씩 set에 추가
                }

                
                if (set.size() == 10) {
                    sb.append("#").append(tc).append(" ").append(result).append("\n");
                    break;
                }

                result = N * (k++);
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}
