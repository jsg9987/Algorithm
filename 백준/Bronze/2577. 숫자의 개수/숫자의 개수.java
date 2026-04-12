import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int A = Integer.parseInt(br.readLine().trim());
		int B = Integer.parseInt(br.readLine().trim());
		int C = Integer.parseInt(br.readLine().trim());
		
		int multipleResult = A * B * C;
		int[] cntArr = new int[10];
		String str = String.valueOf(multipleResult);
		
		
		StringBuilder sb = new StringBuilder();
		
		// 결과 문자열의 첫번째 숫자부터 카운팅
		for(int i = 0; i < str.length(); i++) {
			int curNum = str.charAt(i) - '0';
			
			// 카운팅 배열 index로 사용
			cntArr[curNum]++;
		}
		
		for(int i = 0; i < cntArr.length; i++) {
			sb.append(cntArr[i]).append("\n");
		}
		
		bw.write(sb.toString());
		bw.flush();
		bw.close();
		br.close();
	}
}