import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Solution {
    static HashSet<Integer> set;
    static int N;

    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int T = Integer.parseInt(br.readLine().trim());

        for (int tc = 1; tc < T + 1; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            N = Integer.parseInt(st.nextToken()); // 숫자 개수 8 <= N <= 28
            int K = Integer.parseInt(st.nextToken()); // K번째 큰 수 (생성가능한 수보다 작음)
            set = new HashSet<>();

            char[] arr = new char[N];

            String input = br.readLine().trim();
            for (int i = 0; i < N; i++) {
                arr[i] = input.charAt(i);
            }

            int numPartition = N / 4;
            for (int i = 0; i < numPartition; i++) {
                char[] copy = new char[N];

                for (int j = 0; j < N; j++) {
                    if (j == 0) {
                        copy[j] = arr[N - 1];
                        continue;
                    }
                    copy[j] = arr[j - 1];
                }
                
                getHex(copy);
                arr = copy;
            }
            
            Integer[] passwords = set.toArray(new Integer[0]);
            Arrays.sort(passwords, Comparator.reverseOrder());
            
            bw.write(String.format("#%d %d\n",tc, passwords[K-1]));
            bw.flush();
        }
        bw.close();
        br.close();
    }

    static void getHex(char[] copy) {
        for (int i = 0; i < N; i = i + N / 4) {
            String hexNum = "";
            for (int j = 0; j < N / 4; j++) {
                hexNum += copy[i + j];
            }
            set.add(Integer.parseInt(hexNum, 16));
        }
    }
}