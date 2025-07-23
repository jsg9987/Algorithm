import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;
import java.util.StringTokenizer;

// 풀이 아이디어: 큐를 이용해 다양한 작업을 테스트함.
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        Deque<Integer> q = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer command;

        while (n-- > 0) {
            command = new StringTokenizer(br.readLine(), " ");

            switch (command.nextToken()) {
                // 큐 맨 뒤에 요소 삽입
                case "push":
                    q.offer(Integer.parseInt(command.nextToken()));
                    break;

                // poll은 앞 요소를 삭제, 삭제할 원소가 없을 경우 예외를 던지지 않고 null반환
                case "pop":
                    Integer item = q.poll();
                    if (item == null) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(item).append('\n');
                    }
                    break;

                // size를 반환
                case "size":
                    sb.append(q.size()).append('\n');
                    break;

                // 큐가 비었으면 1, 아니면 0
                case "empty":
                    if (q.isEmpty()) {
                        sb.append(1).append('\n');
                    } else {
                        sb.append(0).append('\n');
                    }
                    break;

                // peek()은 큐에 꺼낼 요소가 없을 경우 null을 반환
                case "front":
                    Integer item2 = q.peek();
                    if (item2 == null) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(item2).append('\n');
                    }
                    break;

                    // peekLast()도 꺼낼 요소가 없을 경우 null 반환
                case "back":
                    Integer item3 = q.peekLast();
                    if (item3 == null) {
                        sb.append(-1).append('\n');
                    } else {
                        sb.append(item3).append('\n');
                    }
                    break;
            }
        }
        System.out.println(sb);
    }
}