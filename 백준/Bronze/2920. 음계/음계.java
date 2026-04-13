import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		StringTokenizer st = new StringTokenizer(br.readLine().trim());
		int increaseCnt = 0;
		int decreaseCnt = 0;
		int[] arr = new int[8];
		
		int idx = 0;
		while(st.hasMoreTokens()) {
			arr[idx++] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 0; i < arr.length - 1; i++) {
			if(arr[i] < arr[i+1]) {
				increaseCnt++;
			} else if(arr[i] > arr[i+1]) {
				decreaseCnt++;
			}
		}
		
		if(increaseCnt == 7) {
			bw.write("ascending");
		} else if(decreaseCnt == 7) {
			bw.write("descending");
		} else {
			bw.write("mixed");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}
}