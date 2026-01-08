import java.io.*;
import java.util.ArrayDeque;
import java.util.Deque;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        String str = br.readLine();
        int M = Integer.parseInt(br.readLine());
        
        Deque<Character> left = new ArrayDeque<>();
        Deque<Character> right = new ArrayDeque<>();
        
        for (int i = 0; i < str.length(); i++) {
            left.addLast(str.charAt(i));
        }
        
        for (int i = 0; i < M; i++) {
            String command = br.readLine();
            char c = command.charAt(0);
            
            switch (c) {
                case 'L': 
                    if (!left.isEmpty()) {
                        right.addFirst(left.removeLast());
                    }
                    break;
                case 'D':
                    if (!right.isEmpty()) {
                        left.addLast(right.removeFirst());
                    }
                    break;
                case 'B': 
                    if (!left.isEmpty()) {
                        left.removeLast();
                    }
                    break;
                case 'P': 
                    left.addLast(command.charAt(2));
                    break;
            }
        }
        
        for (char c : left) {
            bw.write(c);
        }
        for (char c : right) {
            bw.write(c);
        }
        
        bw.flush();
        bw.close();
    }
}