
// 풀이 시간 및 주석: 22:07 ~ 22:24
// 핵심 아이디어: 2차원 배열 int[100][100]에 색종이가 있는 곳을 갱신해서 검은색인 곳을 저장하자.
// 시간: / 메모리: / 난이도 실버5

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); // 인풋 반복 횟수
        int[][] arr = new int[100][100]; // 색종이 채울 배열
        int result = 0;

        for(int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            // 입력의 의미는 왼쪽 꼭짓점을 의미한다.
            int left = Integer.parseInt(st.nextToken()); // 왼쪽 변까지 거리
            int under = Integer.parseInt(st.nextToken()); // 아래 변까지 거리

            for(int j = under; j < under + 10; j++) {
                for(int k = left; k < left + 10; k++) {
                    arr[j][k] = 1;
                }
            }
        }

        for(int i = 0; i < 100; i++) {
            for(int j = 0; j < 100; j++) {
                if (arr[i][j] == 1) {
                    result++;
                }
            }
        }

        System.out.println(result);
    }
}