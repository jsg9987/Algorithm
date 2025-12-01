import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입출력 최적화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 1. N 입력 (수열의 길이)
        int N = Integer.parseInt(br.readLine());

        int[] A = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

        boolean[] visited = new boolean[100001];

        // 4. 투 포인터와 결과 변수 초기화
        long totalCount = 0;
        int R = 0; 
        
        // L 포인터를 0부터 N-1까지 이동
        for (int L = 0; L < N; L++) {
            while (R < N && !visited[A[R]]) {
                visited[A[R]] = true; // A[R]을 부분 수열에 포함시키고 방문 처리
                R++; 
            }

            totalCount += (R - L);


            visited[A[L]] = false;
        }

        System.out.println(totalCount);
    }
}