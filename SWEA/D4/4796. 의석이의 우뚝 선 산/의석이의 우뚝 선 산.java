import java.util.Scanner;

public class Solution {
    static int N;
    static int[] arr;
    static long result; // 가지 수가 int 범위 넘어갈 수 있으니 long 사용

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int tc = 1; tc <= T; tc++) {
            N = sc.nextInt();
            arr = new int[N];
            result = 0;

            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }

            // 투포인터
            for (int i = 1; i < N - 1; i++) {
                // 산 정상 조건
                if (arr[i] > arr[i - 1] && arr[i] > arr[i + 1]) {
                    int left = 0, right = 0;

                    // 왼쪽 길이 구하기
                    int l = i - 1;
                    while (l >= 0 && arr[l] < arr[l + 1]) {
                        left++;
                        l--;
                    }

                    // 오른쪽 길이 구하기
                    int r = i + 1;
                    while (r < N && arr[r] < arr[r - 1]) {
                        right++;
                        r++;
                    }

                    result += (long) left * right;
                }
            }

            System.out.println("#" + tc + " " + result);
        }

        sc.close();
    }
}
