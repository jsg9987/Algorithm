
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution {
	static int M, A;
	static int[] moveA, moveB;
	static int[][] bc;
	static int[] dx = { 0, -1, 0, 1, 0 };
	static int[] dy = { 0, 0, 1, 0, -1 };

	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= T; tc++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            M = Integer.parseInt(st.nextToken());
            A = Integer.parseInt(st.nextToken());

            moveA = new int[M + 1]; // 0초 포함
            moveB = new int[M + 1];
            
            st = new StringTokenizer(br.readLine());
            StringTokenizer st2 = new StringTokenizer(br.readLine());
            for(int i = 1; i <= M; i++) {
            	moveA[i] = Integer.parseInt(st.nextToken());
            	moveB[i] = Integer.parseInt(st2.nextToken());
            }
            
            bc = new int[A][4]; // x, y, c, p
            for(int i = 0; i < A; i++) {
            	st = new StringTokenizer(br.readLine());
            	int y = Integer.parseInt(st.nextToken());
            	int x = Integer.parseInt(st.nextToken());
                int c = Integer.parseInt(st.nextToken());
                int p = Integer.parseInt(st.nextToken());
                bc[i][0] = x - 1;
                bc[i][1] = y - 1;
                bc[i][2] = c;
                bc[i][3] = p;
            }
            
            int ax = 0, ay = 0; // A 시작 (0,0)
            int bx = 9, by = 9; // B 시작 (9,9)
            int result = 0;
            
            for (int t = 0; t <= M; t++) {
                // 현재 위치 충전
                result += getCharge(ax, ay, bx, by);

                // 다음 이동
                if (t < M) {
                    ax += dx[moveA[t + 1]];
                    ay += dy[moveA[t + 1]];
                    bx += dx[moveB[t + 1]];
                    by += dy[moveB[t + 1]];
                }
            }

            System.out.println("#" + tc + " " + result);
        }
	}
        
     // 현재 위치에서 충전 가능한 최대 합
        static int getCharge(int ax, int ay, int bx, int by) {
            int max = 0;
            for (int i = 0; i < A; i++) {
                int aPower = inRange(ax, ay, i) ? bc[i][3] : 0;
                for (int j = 0; j < A; j++) {
                    int bPower = inRange(bx, by, j) ? bc[j][3] : 0;

                    int total;
                    if (i == j && aPower > 0 && bPower > 0) { // 같은 BC 사용
                        total = aPower; // 공유
                    } else {
                        total = aPower + bPower;
                    }
                    max = Math.max(max, total);
                }
            }
            return max;
        }

        static boolean inRange(int x, int y, int idx) {
            int dist = Math.abs(x - bc[idx][0]) + Math.abs(y - bc[idx][1]);
            return dist <= bc[idx][2];
        }
}