import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

	static class Node {
		char value;
		Node left;
		Node right;

		public Node(char value, Node left, Node right) {
			this.value = value;
			this.left = left;
			this.right = right;
		}
	}

	static void insertNode(Node temp, char root, char left, char right) {
		// root가 동일한 경우는 노드를 새로 삽입하는 경우 -> left, right가 있을 경우에 자식 노드 생성('.'이면 생성 안함)
		if (temp.value == root) {
//			temp.left = new Node(root, null, null);
//			temp.right = new Node(root, null, null);
			temp.left = (left == '.' ? null : new Node(left, null, null));
			temp.right = (right == '.' ? null : new Node(right, null, null));

		} else { // 자식 노드인지 확인 후 재귀로 삽입
			if (temp.left != null)
				insertNode(temp.left, root, left, right);
			if (temp.right != null)
				insertNode(temp.right, root, left, right);
		}
	}
	
	// root -> left -> right
	static void preOrder(Node head) {
		if(head == null) return;
		System.out.print(head.value);
		preOrder(head.left);
		preOrder(head.right);
	}
	
	// left -> root -> right
	static void inOrder(Node head) {
		if(head == null) return;
		inOrder(head.left);
		System.out.print(head.value);
		inOrder(head.right);
	}
	
	// left -> right -> root
	static void postOrder(Node head) {
		if(head == null) return;
		postOrder(head.left);
		postOrder(head.right);
		System.out.print(head.value);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		Node head = new Node('A', null, null);

		for (int i = 0; i < n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			char root = st.nextToken().charAt(0);
			char left = st.nextToken().charAt(0);
			char right = st.nextToken().charAt(0);
			insertNode(head, root, left, right);
		}

		preOrder(head);
		System.out.println();
		inOrder(head);
		System.out.println();
		postOrder(head);
	}
}