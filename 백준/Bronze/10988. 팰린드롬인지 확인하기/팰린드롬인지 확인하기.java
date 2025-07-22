import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        // 1. 문자열 붙이기
//        String reverse = "";
//        for (int i = s.length() - 1; i >= 0; i--) {
//            reverse = reverse + s.charAt(i);
//        }

        // 2. StringBuffer 사용하기
        StringBuffer sb = new StringBuffer(s);
        String reverse = sb.reverse().toString();

        // 3. 결과 출력
        if (s.equals(reverse)) {
            System.out.println(1);
        }else {
            System.out.println(0);
        }
    }
}