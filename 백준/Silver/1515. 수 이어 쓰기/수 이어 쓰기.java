import java.io.*;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String input = br.readLine().trim();
		int len = input.length();
		int[] start = new int[len];
		
		for(int i = 0; i < len; i++) {
			start[i] = input.charAt(i) - '0';
		}
		
		int num = 0;
		int idx = 0;
		
		while(idx < len) {
			num++;
			String temp = String.valueOf(num);
			
			for(int i = 0; i < temp.length(); i++) {
				if(idx < len && temp.charAt(i) - '0' == start[idx]) {
					idx++;
				}
			}
		}
		
		bw.write(String.valueOf(num));
		bw.flush();
		bw.close();
		br.close();
	}
}
