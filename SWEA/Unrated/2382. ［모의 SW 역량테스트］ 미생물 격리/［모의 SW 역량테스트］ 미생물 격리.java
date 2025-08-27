import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.StringTokenizer;

/*
 * tc: 50, 5초, 256MB, 5<=N<=100, 5<=k<=1,000, 1<=M<=1,000
 */

class Node {
	int x;
	int y;
	int count;
	int dir;

	public Node(int x, int y, int count, int dir) {
		super();
		this.x = x;
		this.y = y;
		this.count = count;
		this.dir = dir;
	}

	@Override
	public String toString() {
		return "Node [x=" + x + ", y=" + y + ", count=" + count + ", dir=" + dir + "]";
	}
}

public class Solution {
	static int N;
	static int[][] board;
	static Node[] nodes;
	static int[] dx = { -1, 1, 0, 0 };
	static int[] dy = { 0, 0, -1, 1 };

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//		StringBuilder sb = new StringBuilder();

		int T = Integer.parseInt(br.readLine().trim());
		for (int tc = 1; tc < T + 1; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine().trim());
			N = Integer.parseInt(st.nextToken());
			board = new int[N][N];
			int M = Integer.parseInt(st.nextToken());
			int K = Integer.parseInt(st.nextToken());
			nodes = new Node[K];

			// board 테두리 구역 세팅
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < N; j++) {
					if (i == 0 || i == N - 1 || j == 0 || j == N - 1) {
						board[i][j] = -1;
					}
				}
			}

			// 노드 배열 초기화
			for (int i = 0; i < K; i++) {
				st = new StringTokenizer(br.readLine().trim());
				int x = Integer.parseInt(st.nextToken());
				int y = Integer.parseInt(st.nextToken());
				int count = Integer.parseInt(st.nextToken());
				int dir = Integer.parseInt(st.nextToken()) - 1;
				nodes[i] = new Node(x, y, count, dir);
			}

//			System.out.println(Arrays.toString(nodes));

			// M시간 동안
			for (int m = 0; m < M; m++) {
				// 각 노드들 이동시키기, 테두리 닿으면 값 변경하고 방향 바꾸기
				for (int j = 0; j < K; j++) {
					if (nodes[j] == null)
						continue;
					int dir = nodes[j].dir;
					int nx = nodes[j].x + dx[dir];
//					System.out.println("nx: "+ nx);
					int ny = nodes[j].y + dy[dir];
//					System.out.println("ny: " + ny);
					int count = nodes[j].count;

					if (isIn(nx, ny)) {
						// 테두리에 닿은 경우
						if (board[nx][ny] == -1) {
							count /= 2;
							if (dir == 0)
								dir = 1;
							else if (dir == 1)
								dir = 0;
							else if (dir == 2)
								dir = 3;
							else if (dir == 3)
								dir = 2;
							nodes[j].x = nx;
							nodes[j].y = ny;
							nodes[j].count = count;
							nodes[j].dir = dir;
						} else if (board[nx][ny] == 0) { // 아닌 경우
							nodes[j].x = nx;
							nodes[j].y = ny;
							nodes[j].count = count;
							nodes[j].dir = dir;
						}
					}
				}

//				System.out.println("이동 마치고 위치: " + Arrays.toString(nodes));
				int maxMicrobeIdx[][][] = new int[N][N][3]; 
				// 0: sum, 1: maxIdx, 2: maxCount

				for (int i = 0; i < N; i++) {
				    for (int j = 0; j < N; j++) {
				        maxMicrobeIdx[i][j][1] = -1; // maxIdx 초기화
				    }
				}

				for (int j = 0; j < K; j++) {
				    if (nodes[j] == null) continue;
				    Node node = nodes[j];
				    int x = node.x, y = node.y, count = node.count;

				    // 합계 누적
				    maxMicrobeIdx[x][y][0] += count;

				    // 더 큰 군집 기준으로 대표자 교체
				    if (count > maxMicrobeIdx[x][y][2]) {
				        maxMicrobeIdx[x][y][2] = count;
				        maxMicrobeIdx[x][y][1] = j;
				    }
				}

				// 최종 갱신
				for (int j = 0; j < K; j++) {
				    if (nodes[j] == null) continue;
				    int x = nodes[j].x, y = nodes[j].y;

				    if (maxMicrobeIdx[x][y][1] == j) {
				        // 대표 노드 -> 합계와 dir 반영
				        nodes[j].count = maxMicrobeIdx[x][y][0];
				    } else {
				        // 대표 아닌 노드 제거
				        nodes[j] = null;
				    }
				}

			}

//				System.out.println("=== 한사이클 종료===");
//				System.out.println("Nodes 출력: " + Arrays.toString(nodes));

			// M시간이 지나고 난 후 미생물 수 return
			int result = 0;
			for (int i = 0; i < K; i++) {
				if (nodes[i] != null) {
					result += nodes[i].count;
				}
			}
//			System.out.println(result);

			String output = String.format("#%d %d\n", tc, result);
			bw.write(output);
			bw.flush();
		}
		bw.flush();
		bw.close();
		br.close();

	}

	static boolean isIn(int x, int y) {
		return x >= 0 && x < N && y >= 0 && y < N;
	}
}