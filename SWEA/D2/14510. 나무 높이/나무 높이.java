import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        
        for(int tc = 1; tc < T+1; tc++) {
            int N = Integer.parseInt(br.readLine().trim());
            int[] arr = new int[N];
            int maxValue = Integer.MIN_VALUE;
            int one = 0;
            int two = 0;
            int cnt = 0;
            StringTokenizer st = new StringTokenizer(br.readLine().trim());
            for(int i = 0; i < N; i++) {
                arr[i] = Integer.parseInt(st.nextToken());
                maxValue = Math.max(maxValue, arr[i]);
            }
            
            // 최대 높이와 차 구해서 업데이트하기 & one, two 개수 구하기
            for(int i = 0; i < N; i++) {
                arr[i] = maxValue - arr[i];    
                one += arr[i] % 2;
                two += arr[i] / 2;
            }
            
            // one, two 비율 조정하기
            int diff = two - one;
            if(diff >= 3) {
            	one += diff / 3 * 2;
            	two -= diff / 3;
            }
            
            if(one > two) {
            	cnt += two * 2;
            	one -= two;
            	cnt += one * 2 -1;
            }else if(two > one) {
            	cnt += one * 2;
            	two -= one;
            	if(two == 1) {
            		cnt += 2;
            	}else if(two == 2) {
            		cnt += 3;
            	}
            }else {
            	cnt += one * 2;
            }
            
            System.out.printf("#%d %d\n", tc, cnt);
        }
        
    }
}
