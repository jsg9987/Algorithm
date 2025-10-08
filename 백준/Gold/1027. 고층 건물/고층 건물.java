import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine().trim());
		int[] arr = new int[N];

		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		for (int i = 0; i < N; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		int globalMax = 0;
		for (int idx = 0; idx < N; idx++) {
			int tempMax = 0;
			for (int arrival = 0; arrival < N; arrival++) {
				double dx = arrival - idx;
				double dy = arr[arrival] - arr[idx];
				double gradient = dy / dx;
				double y_intercept = arr[idx] - gradient * idx;

				boolean flag = true;
				if (idx < arrival) {
					for (int i = idx + 1; i < arrival; i++) {
//						System.out.println("start: " + idx);
//						System.out.println("end: " + arrival);
//						System.out.println(gradient * i + y_intercept);
						if ((gradient * i + y_intercept) <= arr[i]) {
							flag = false;
						}
					}
				}else {
					for (int i = arrival+1; i < idx; i++) {
//						System.out.println("start: " + idx);
//						System.out.println("end: " + idx);
//						System.out.println(gradient * i + y_intercept);
						if ((gradient * i + y_intercept) <= arr[i]) {
							flag = false;
						}
					}
				}

				if (flag && idx != arrival) {
					tempMax++;
				}
			}
//			System.out.println(idx + "의 최대 볼 수 있는 빌딩 개수" + tempMax);
			globalMax = Math.max(globalMax, tempMax);
		}

		System.out.println(globalMax);
	}
}