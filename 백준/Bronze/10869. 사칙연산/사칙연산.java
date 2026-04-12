import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // input이 공백으로 주어짐.
        String data = br.readLine();
        StringTokenizer st = new StringTokenizer(data);
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

    System.out.println(a+b);
    System.out.println(a-b);
    System.out.println(a*b);
    System.out.println(a/b);
    System.out.println(a%b);
}
}