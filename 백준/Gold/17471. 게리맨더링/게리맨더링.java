import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

/*
 * 
 * 복기
 * - 문제점
 * 1. 부분조합 로직을 잘못 작성함.
 * nowCnt로 
 * 2. bfs에서 선거구를 확인할 때 자신의 선거구가 아닐 때도 퍼져나가게 해버림.
 * 문제에서 "중간에 통하는 인접한 구역은 모두 같은 선거구에 포함된 구역이어야 한다"라고 했다. 이 말은 선거구에 속한 정점들로만 경로를 정해야한다는 것이다.
 * 따라서 내 로직에서 코드를 간단하게 하기 위해 bfs가 그냥 퍼지게 한 후 지역구 정점들이 포함되는지만 확인하면 안되고 같은 지역구 정점이 아니라면 못퍼지게 제어해야함.
 * 
 */
public class Main {
    static int[] population;
    static List<List<Integer>> graph;
    static boolean[] visited;
    static int N;
    static int minValue;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb = new StringBuilder();

        N = Integer.parseInt(br.readLine().trim());
        population = new int[N + 1];
        graph = new ArrayList<>();
        visited = new boolean[N + 1];
        minValue = Integer.MAX_VALUE;

        for (int i = 0; i < N + 1; i++) {
            graph.add(new ArrayList<>());
        }

        StringTokenizer st = new StringTokenizer(br.readLine().trim());

        for (int i = 1; i < N + 1; i++) {
            population[i] = Integer.parseInt(st.nextToken());
        }

        // 인접리스트 생성
        for (int i = 1; i < N + 1; i++) {
            st = new StringTokenizer(br.readLine().trim());
            int repeat = Integer.parseInt(st.nextToken());
            for (int j = 0; j < repeat; j++) {
                int child = Integer.parseInt(st.nextToken());
                graph.get(i).add(child);
                graph.get(child).add(i);
            }
        }

        for (int i = 1; i < N / 2 + 1; i++) {
        	// 돌 떄마다 visited 초기화
        	Arrays.fill(visited, false);
            dfs(i, 0, 1);
        }
        
        if(minValue == Integer.MAX_VALUE) minValue = -1;
        
        sb.append(minValue).append("\n");
        bw.write(sb.toString());
        
        bw.flush();
        bw.close();
        br.close();
    }

    static void dfs(int cnt, int nowCnt, int idx) {
        // 기저 조건: 부분조합 개수만큼 다 골랐을 때 bfs
        if (nowCnt == cnt) {
            int one = 0, two = 0;
            for(int i = 1; i < N+1; i++) {
                if(visited[i]) {
                    one += population[i];
                }else {
                    two += population[i];
                }
            }
            if(Math.abs(one - two) >= minValue) return;
            bfs();
            return;
        }

        // idx 벗어났을 때
        if (idx >= N + 1)
            return;

        for (int i = idx; i < N + 1; i++) {
            // 포함
            visited[i] = true;
            dfs(cnt, nowCnt + 1, i+1);
            visited[i] = false;

            // 비포함 -> 필요없음. nowCnt로 부분집합 개수를 제어하고 있기 때문에 아래 코드는 중복 탐색됨.
//            dfs(cnt, nowCnt, i+1);
        }
    }

    static void bfs() {
        // 2가지 집합으로 나누기
        ArrayList<Integer> first = new ArrayList<>();
        ArrayList<Integer> second = new ArrayList<>();

        for (int i = 1; i < N + 1; i++) {
            if (visited[i] == true) {
                first.add(i);
            } else {
                second.add(i);
            }
        }

        // 나눈 집합이 구역 분할이 되는지, 최소값이 더 작은지 체크
        boolean[] firstCheck = new boolean[N + 1];
        boolean[] secondCheck = new boolean[N + 1];

        Queue<Integer> firstQ = new ArrayDeque<>();
        Queue<Integer> secondQ = new ArrayDeque<>();

        int one = first.get(0);
        int two = second.get(0);

        firstQ.offer(first.get(0));
        firstCheck[one] = true;
        secondQ.offer(second.get(0));
        secondCheck[two] = true;

        // bfs 탐색
        while (!firstQ.isEmpty()) {
            int now = firstQ.poll();

            for (int e : graph.get(now)) {
                if (!firstCheck[e] && visited[e]) { // 같은 선거구인지도 visited롤 통해 확인 필요
                    firstCheck[e] = true;
                    firstQ.offer(e);
                }
            }
        }

        // 분할됐는지 검사
        for (int e : first) {
            if (!firstCheck[e])
                return;
        }
        
        while (!secondQ.isEmpty()) {
            int now = secondQ.poll();

            for (int e : graph.get(now)) {
                if (!secondCheck[e] && !visited[e]) {
                    secondCheck[e] = true;
                    secondQ.offer(e);
                }
            }
        }


        for (int e : second) {
            if (!secondCheck[e])
                return;
        }
        
//        System.out.println("===새로운 케이스===");
//        System.out.println(Arrays.toString(firstCheck));
//        System.out.println(Arrays.toString(secondCheck));

        // 최소인지 검사
        int sum1 = 0, sum2 = 0;
        for (int e : first) {
            sum1 += population[e];
        }

        for (int e : second) {
            sum2 += population[e];
        }
//        System.out.println(first.toString());
//        System.out.println(second.toString());
//        System.out.println("이번 케이스 합차: " + Math.abs(sum1 - sum2));
        minValue = Math.min(minValue, Math.abs(sum1 - sum2));
        return;
    }
}