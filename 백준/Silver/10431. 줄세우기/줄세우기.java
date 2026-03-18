import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int P = Integer.parseInt(br.readLine().trim());

        for (int i = 0; i < P; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            int T = Integer.parseInt(st.nextToken()); // test case 번호

            int[] students = new int[20];
            for (int j = 0; j < 20; j++) {
                students[j] = Integer.parseInt(st.nextToken());
            }

            int total = 0;
            int[] line = new int[20];
            int lineSize = 0;

            for (int j = 0; j < 20; j++) {
                int student = students[j];
                // 줄에 있는 사람 중 나보다 키 큰 사람 수 = 이동 횟수
                for (int k = 0; k < lineSize; k++) {
                    if (line[k] > student) {
                        total++;
                    }
                }
                line[lineSize++] = student;
            }

            bw.write(T + " " + total + "\n");
        }

        bw.flush();
        bw.close();
    }
}