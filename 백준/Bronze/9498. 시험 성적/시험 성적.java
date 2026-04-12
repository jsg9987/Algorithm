import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOError;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
//		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int score = Integer.parseInt(st.nextToken());
		char grade = 'A';
		if(score<60	) {
			grade = 'F';
		}else if(score<70) {
			grade = 'D';
		}else if(score<80) {
			grade = 'C';
		}else if(score<90) {
			grade = 'B';
		}else if(score<=100) {
			grade = 'A';
		}else {
			
		}
		System.out.println(grade);
		
		br.close();
				
				
				 
	}
}