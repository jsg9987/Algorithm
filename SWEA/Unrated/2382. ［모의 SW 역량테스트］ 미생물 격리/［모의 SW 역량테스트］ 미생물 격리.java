import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 유형: 시뮬레이션
 * 기능
 * 1. 군집 이동
 * - 1시간마다 군집 이동
 * - 약품 처리: 절반이 죽고, 이동방향이 반대로 바뀜. 0이되면 소멸!
 * - 군집 병합: 두 개 이상의 군집이 한 셀에 모이면 합쳐짐. 이동방향은 max 따라감.
 * 
 */

class Micro {
	int x, y, cnt, dir, total;
	boolean isDead;

	public Micro(int x, int y, int cnt, int dir) {
		super();
		this.x = x;
		this.y = y;
		this.total = this.cnt = cnt;
		this.dir = dir;
	}
}

public class Solution {
	static int[] dx = { 0, -1, 1, 0, 0 };
	static int[] dy = { 0, 0, 0, -1, 1 };
	static int N;
	static Micro[][] board;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine().trim());
		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());

			N = Integer.parseInt(st.nextToken()); // 셀의 개수 5 <= N <= 100
			int M = Integer.parseInt(st.nextToken()); // 시간 1 <= M <= 1000
			int K = Integer.parseInt(st.nextToken()); // 군집 수 5 <= K <= 1000
			Micro[] micros = new Micro[K];
			board = new Micro[N][N]; // board

			// K개의 군집 받기
			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine().trim());
				// x,y,cnt, dir
				micros[i] = new Micro(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()),
						Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
			}

			int result = 0;

			// 1. M시간동안 진행
			for (int time = 0; time < M; time++) {
				for (int i = 0; i < K; i++) {
					if (micros[i].isDead)
						continue; // 죽었으면 건너뜀

					Micro now = micros[i];

					// 2. 군집들 한칸 이동
					int nx = now.x + dx[now.dir];
					int ny = now.y + dy[now.dir];

					// 3. 약품 처리(반 줄이고 반대방향)
					if (nx == 0 || nx == N - 1 || ny == 0 || ny == N - 1) {
						now.total = now.cnt /= 2; // total 값도 줄여야함.
						// 죽었을 때 처리
						if (now.cnt == 0) {
							now.isDead = true;
							continue;
						}

						if (now.dir % 2 == 0)
							now.dir -= 1;
						else
							now.dir += 1;
					}
					now.x = nx;
					now.y = ny;

					// 4. 병합: 처음일 때랑 2개 이상 만날 때
					if (board[nx][ny] == null) {
						board[nx][ny] = now;
					} else {
						Micro exist = board[nx][ny];

						// 이미 존재하던 군집이 큰경우
						if (exist.cnt > now.cnt) {
							board[nx][ny].total += now.cnt;
							now.isDead = true; // now 없애기
						} else {
							// now가 큰 경우:board에 now를 넣고 now 정보를 갱신
							now.total += board[nx][ny].total;
							board[nx][ny].isDead = true;
							board[nx][ny] = now;
						}
					}

				}
				// micros 갱신
				result = reset();
			}

			System.out.printf("#%d %d\n", tc, result);
		}

	}

	// map 초기화 및 cnt 갱신
	static int reset() {
		int result = 0;
		for (int r = 0; r < N; r++) {
			for (int c = 0; c < N; c++) {
				if (board[r][c] == null)
					continue;
				// 존재한다면
				board[r][c].cnt = board[r][c].total;
				result += board[r][c].total;
				board[r][c] = null;
			}
		}

		return result;
	}
}