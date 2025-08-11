import java.io.FileInputStream;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Queue;
import java.util.StringTokenizer;

import java.io.FileNotFoundException;

public class Main {

	static int N;
	static ArrayList<Integer>[] graph;
	static boolean[] visited;
	static int groupCnt = 0;
	
	public static void main(String[] args) throws FileNotFoundException, IOException {
		//System.setIn(new FileInputStream("Test3.txt"));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		visited = new boolean[N+1];
		graph = new ArrayList[N+1];
		
		for(int i = 0; i < N+1; i++) {
			graph[i] = new ArrayList<Integer>();
		}
		
		for(int i = 1; i < M+1; i++) {
			st = new StringTokenizer(br.readLine());
			int u = Integer.parseInt(st.nextToken());
			int v = Integer.parseInt(st.nextToken());
			graph[u].add(v);
			graph[v].add(u);
		}
		
		for(int i = 1; i < N+1; i++) {
			bfs(i);
		}
		
		System.out.println(groupCnt);
	}
	
	public static void bfs(int idx) {
		if(visited[idx]) {
			return;
		}
		
		Queue<Integer> q = new ArrayDeque<>();
		visited[idx] = true;
		q.offer(idx);
		groupCnt++;
		
		while(!q.isEmpty()) {
			int nodeIdx = q.poll();
			
			for(int e : graph[nodeIdx]) {
				if(!visited[e]) {
					visited[e] = true;
					q.offer(e);
				}
			}
		}
		
	}
}
