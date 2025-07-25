import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력 처리
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] nums = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(nums);  // 오름차순 정렬
        int result = 0;

        // 각 숫자에 대해 "좋은 수"인지 검사
        for (int i = 0; i < n; i++) {
            int left = 0;
            int right = n - 1;

            while (left < right) {
                // 현재 검사 중인 수(nums[i])는 제외
                if (left == i) {
                    left++;
                    continue;
                }
                if (right == i) {
                    right--;
                    continue;
                }

                int sum = nums[left] + nums[right];

                if (sum == nums[i]) {
                    result++;
                    break;
                } else if (sum < nums[i]) {
                    left++;
                } else {
                    right--;
                }
            }
        }

        System.out.println(result);
    }
}
