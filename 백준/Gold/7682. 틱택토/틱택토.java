import java.io.*;
import java.util.*;

public class Main {
	static char[][] board;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

		String input = br.readLine().trim();

		while (!input.equals("end")) {
			board = new char[3][3];
			int oCnt = 0;
			int xCnt = 0;
			int cnt = 0;

			for (int i = 0; i < 3; i++) {
				for (int j = 0; j < 3; j++) {
					char temp = input.charAt(cnt);
					if (temp == 'O') {
						oCnt++;
					} else if (temp == 'X') {
						xCnt++;
					}
					board[i][j] = temp;
					cnt++;
				}
			}
			
			boolean xWin = check('X');
			boolean oWin = check('O');
			
			boolean flag = false;

			// O가 이긴 경우(X는 이기면 안됨.)
			if (oCnt == xCnt) {
				if(!xWin && oWin) {
					flag = true;
				}
			} else if (xCnt - oCnt == 1) { // X가 이긴 경우(O는 이기면 안됨.)
				if (xWin && !oWin) {
					flag = true;
				} else if(!xWin && !oWin && xCnt == 5 && oCnt == 4) { // 무승부 꽉찬 경우
					flag = true;
				}
			}

			if (flag) {
				bw.write("valid");
				bw.write("\n");
			} else {
				bw.write("invalid");
				bw.write("\n");
			}

			input = br.readLine().trim();
		}

		bw.flush();
		bw.close();
		br.close();
	}

	private static boolean check(char c) {
		boolean flag = false;
		// 가로
		for(int i = 0; i < 3; i++) {
			if(board[i][0] != c) continue;
			if(board[i][1] != c) continue;
			if(board[i][2] != c) continue;
			
			flag = true;
		}
		
		// 세로
		for(int i = 0; i < 3; i++) {
			if(board[0][i] != c) continue;
			if(board[1][i] != c) continue;
			if(board[2][i] != c) continue;
			
			flag = true;
			break;
		}
		
		if((board[0][0] == c) && (board[1][1] == c) && (board[2][2] == c)) {
			flag = true;
		}
		
		if((board[0][2] == c) && (board[1][1] == c) && (board[2][0] == c)) {
			flag = true;
		}
		
		return flag;
	}

	private static boolean isIn(int nx, int ny) {
		return nx >= 0 && nx < 3 && ny >= 0 && ny < 3;
	}
}
