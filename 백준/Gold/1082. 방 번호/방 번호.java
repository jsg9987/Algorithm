import java.io.*;
import java.util.*;

public class Main {

    static String maxString(String s1, String s2) {
        if (s1 == null || s1.length() == 0) {
            return s2;
        }
        if (s2 == null || s2.length() == 0) {
            return s1;
        }

        if (s1.length() > s2.length()) {
            return s1;
        } else if (s1.length() < s2.length()) {
            return s2;
        } else {
            if (s1.compareTo(s2) > 0) {
                return s1;
            } else {
                return s2;
            }
        }
    }

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine().trim()); 
        
        int[] cost = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        for (int i = 0; i < N; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }
        
        int M = Integer.parseInt(br.readLine().trim()); 

        String[] DP = new String[M + 1];

        Arrays.fill(DP, "");
        
        for (int i = 1; i <= M; i++) {
            for (int j = 0; j < N; j++) {
                int currentCost = cost[j];
                
                if (i >= currentCost) {
                    
                    String prevNum = DP[i - currentCost];
                    
                    if (prevNum.length() == 0 && j == 0) {
                        continue;
                    }

                    String newNum = prevNum + String.valueOf(j);
                    
                    DP[i] = maxString(DP[i], newNum);
                }
            }
        }

        if (DP[M].length() == 0) {
             System.out.println("0");
        } else {
             System.out.println(DP[M]);
        }
    }
}
