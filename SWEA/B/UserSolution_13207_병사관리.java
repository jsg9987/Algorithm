/*
 * API를 시간 안에 실행할 수 있도록 보통 입력값 상한이 큰건 O(1), 작은 건 O(N)이 되도록 자료구조와 알고리즘 선택해야함.
 */
class UserSolution_13207_병사관리 {
	public class Node {
		int id;
		int v;
		Node nxt; // LinkedList로 사용하기 위해서

		Node() {
		}

		Node(int id, int v) {
			this.id = id;
			this.v = v;
			this.nxt = null;
		}

		// 특정 팀을 지정하기 위한 생성자
		Node(int id, int v, Node nxt) {
			this.id = id;
			this.v = v;
			this.nxt = nxt;
		}
	}

	public Node[] node = new Node[200055]; // hire, updateSoldier 연산 + 여유분 55
	public int cnt = 0;
	public int[] version = new int[100055]; // version[i] := ID가 i인 사람의 최신 버전
	public int[] num = new int[100055]; // num[i] := ID가 i인 사람의 team 번호, team번호 저장용

	public Node getNewNode(int id, Node nxt) {
		Node ret = node[cnt++];
		ret.id = id;
		ret.nxt = nxt;
		ret.v = ++version[id];
		return ret;
	}

	public class Team {
		Node[] head = new Node[6];
		Node[] tail = new Node[6];
	}

	// Team 배열 6
	public Team[] t = new Team[6];

	// 전체적으로 초기 세팅을 하고, 고용할 때는 기존 값을 변경하고 변경할 땐 append하겠다는 작전
	public void init() {
		cnt = 0;
		// Node 초기화
		for (int i = 0; i < 200055; i++) {
			if (node[i] == null)
				node[i] = new Node();
		}

		// Team 초기화
		for (int i = 1; i <= 5; i++) {
			t[i] = new Team();
			for (int j = 1; j <= 5; j++) {
				t[i].tail[j] = t[i].head[j] = getNewNode(0, null); // 자기자신을 가리키는 List
			}
		}

		// node 버전, 팀번호 0 세팅
		for (int i = 0; i <= 100000; i++) {
			version[i] = 0;
			num[i] = 0;
		}
	}

	public void hire(int mID, int mTeam, int mScore) { // O(1)
		Node newNode = getNewNode(mID, null);
		t[mTeam].tail[mScore].nxt = newNode;
		t[mTeam].tail[mScore] = newNode;
		num[mID] = mTeam;
	}

	// version: -1, 0, 1
	public void fire(int mID) {
		version[mID] = -1;
	}

	public void updateSoldier(int mID, int mScore) { // O(1)
		hire(mID, num[mID], mScore);
	}

	// 팀 전체 평판 점수를 mChangeScore로 변경
	public void updateTeam(int mTeam, int mChangeScore) { // O(1)
		//
		if (mChangeScore < 0) {
			for (int j = 1; j <= 5; j++) {
				int k = j + mChangeScore;
				k = k < 1 ? 1 : (k > 5 ? 5 : k); // 5보다 작으면 원래 k값
				if (j == k)
					continue; // 점수변화 없으면 건너뜀

				if (t[mTeam].head[j].nxt == null)
					continue; // 비었으면 continue

				// j 버킷(실병사 구간)을 k 버킷 뒤에 '붙인다'
				t[mTeam].tail[k].nxt = t[mTeam].head[j].nxt;
				t[mTeam].tail[k] = t[mTeam].tail[j];
				// j 버킷은 비워서 더미만 남긴다
				t[mTeam].head[j].nxt = null;
				t[mTeam].tail[j] = t[mTeam].head[j];
			}
		}
		if (mChangeScore > 0) {
			for (int j = 5; j >= 1; j--) { // 높은 점수 -> 낮은 점수 순서
				int k = j + mChangeScore;
				k = k < 1 ? 1 : (k > 5 ? 5 : k);
				if (j == k)
					continue;

				if (t[mTeam].head[j].nxt == null)
					continue;

				t[mTeam].tail[k].nxt = t[mTeam].head[j].nxt;
				t[mTeam].tail[k] = t[mTeam].tail[j];

				t[mTeam].head[j].nxt = null;
				t[mTeam].tail[j] = t[mTeam].head[j];
			}
		}
	}

	public int bestSoldier(int mTeam) {
		for (int j = 5; j >= 1; j--) { // 점수 높은 것부터
            Node node = t[mTeam].head[j].nxt; // 해당 점수 버킷 첫 노드
            if (node == null) continue;

            int ans = 0;
            while (node != null) { // 연결 리스트 순회
                if (node.v == version[node.id]) { // 최신 노드만 고려
                    ans = ans < node.id ? node.id : ans; // ID 최대값 갱신
                }
                node = node.nxt; // -> 다음 노드 선택
            }
            if (ans != 0) return ans;
        }
        return 0;
	}
}
