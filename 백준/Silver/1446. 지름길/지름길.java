import java.io.*;
import java.util.*;

public class Main {

    public static class Road implements Comparable<Road> {
        int from, to, length;

        public Road(int from, int to, int length) {
            this.from = from;
            this.to = to;
            this.length = length;
        }

        @Override
        public int compareTo(Road o) {
            return Integer.compare(this.to, o.to); // to 기준 정렬
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine().trim());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());

        ArrayList<Road> roads = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int length = Integer.parseInt(st.nextToken());

            if (to > D || length >= to - from) continue;

            roads.add(new Road(from, to, length));
        }

        Collections.sort(roads);

        int[][] DP = new int[roads.size() + 1][D + 1];
        for (int j = 0; j <= D; j++) {
            DP[0][j] = j; // 지름길을 하나도 안 썼을 때
        }

        for (int i = 0; i < roads.size(); i++) {
            Road r = roads.get(i);
            int from = r.from;
            int to = r.to;
            int len = r.length;

            for (int j = 0; j <= D; j++) {
                // 기본적으로 이전 값 복사
                DP[i + 1][j] = DP[i][j];

                // 지름길을 통해 갱신할 수 있는 거리 j만 갱신
                if (j >= to) {
                    DP[i + 1][j] = Math.min(DP[i + 1][j], DP[i][from] + len + (j - to));
                }
            }
        }

        System.out.println(DP[roads.size()][D]);
    }
}
