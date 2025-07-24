import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        // 빠른 입력을 위해 BufferedReader 사용
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 첫 줄 입력: 보드의 행(n), 열(m)
        String[] nm = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        // 보드 저장할 2차원 배열
        char[][] board = new char[n][m];

        // 보드 입력 받기
        for (int i = 0; i < n; i++) {
            board[i] = br.readLine().toCharArray();
        }

        int minDraw = Integer.MAX_VALUE; // 정답(최소 색칠 수)

        // 모든 8x8 체스판 가능한 위치를 순회
        for (int i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                int draw1 = 0; // 'B'로 시작하는 경우
                int draw2 = 0; // 'W'로 시작하는 경우

                // 해당 8x8 부분 탐색
                for (int row = i; row < i + 8; row++) {
                    for (int col = j; col < j + 8; col++) {
                        // (row + col) 짝수인 경우 → 시작 색
                        if ((row + col) % 2 == 0) {
                            if (board[row][col] != 'B') draw1++;
                            if (board[row][col] != 'W') draw2++;
                        } else {
                            if (board[row][col] != 'W') draw1++;
                            if (board[row][col] != 'B') draw2++;
                        }
                    }
                }

                // 현재 위치의 최소 색칠 수를 전체 최소와 비교
                minDraw = Math.min(minDraw, Math.min(draw1, draw2));
            }
        }

        // 결과 출력
        System.out.println(minDraw);
    }
}

