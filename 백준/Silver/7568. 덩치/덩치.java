import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		// 1. x,y 배열로 각 사람의 키와 몸무게를 저장
		// 2. 첫 사람부터 x,y를 모든사람과 비교해서 (키, 몸무게) 모두 자기보다 크면 자기 등수++
		// 	  (키,몸무게) 모두 자기보다 작으면 등수변화 x
		
		int N = Integer.parseInt(br.readLine().trim()); // N: 전체 사람의 수
		int[] xArr = new int[N];
		int[] yArr = new int[N];
		for(int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			xArr[i] = Integer.parseInt(st.nextToken());
			yArr[i] = Integer.parseInt(st.nextToken());
		}
		
		int[] result = new int[N]; // 등수 배열
		for(int i = 0; i < N; i++) {
			int biggerCnt = 0;
			for(int j = 0; j < N; j++) {
				if(i == j) continue; // idx 같을 때는 skip
				
				if((xArr[i] < xArr[j]) && (yArr[i] < yArr[j])) {
					biggerCnt++;
				}
			}
			
			result[i] = biggerCnt + 1;
		}
		
		StringBuilder sb = new StringBuilder();
		for(int i = 0; i < N; i++) {
			sb.append(result[i]).append(" ");
		}
		
		bw.write(sb.toString().trim());
		bw.flush();
		bw.close();
		br.close();
	}
}