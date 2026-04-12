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
		
		int h = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		if(m>=45) {
			System.out.println(h + " "+ (m-45));
		}else if(m<45 && h ==0){
			System.out.println(23 + " " + (m+15));
		}else {
			System.out.println(h-1 + " " + (m+15));

		}
		
		
		br.close();
				 
	}
}
