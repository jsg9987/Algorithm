/*
 * 항상 마지막 method가 설계할 때 관건인 것 같다. 사용자가 최근 시청한 최대 5개 영화들 중에서 "사용자가 준 평점이 가장 높은 영화"와 "장르"가 같은 영화만 추천
 * max 평점이 여러개면 제일 최근 시청한 영화와 같은 장르로 추천, 시청 목록에 아무영화도 안봤다면 장르 상관 없이 모든 영화에 대해 추천
 * "위 조건 만족하는 영화들 중" "총점이 가장 높은 순으로" "최대 5개 추천"
 * 
 * 1. 시청목록을 배열로 구성? -> 삭제 시 배열을 다시 만들어야함. -> 5000 * 1000 -> 500만
 * 2. 시청목록을 LinkedList로 관리하자. -> erase에서 포인터만 끊고 고립시키면 1000번만 지우면 됨.
 * 3. 사용자가 준 평점, 영화의 총점을 따로 저장 및 관리해야함. 총점이 높은 순서 -> maxHeap?
 * 4. 장르별 maxHeap을 만들자, 장르 상관없이 추천할 경우도 있으니 전체 heap도 만든다.
 *    M: 최대 영화 수 10000번 삽입, add * log(M) == 10000 * 14.xx == 14만
 *    erase * log(M) = 1000 * 14.xx = 1.4만
 *    watch * log(M) = 30000 * 14.xx = 42만
 *    suggest 횟수: 5000
 *    시간복잡도 ok
 */

import java.util.*;

class Movie {
    int mID, mGenre, mTotal;
    boolean removed; // 제거 여부
    Set<Integer> watchedUsers = new HashSet<>();

    Movie(int mID, int mGenre, int mTotal) {
        this.mID = mID;
        this.mGenre = mGenre;
        this.mTotal = mTotal;
        this.removed = false;
    }
}


// 추천 영화 ID 담기
class RESULT {
    int cnt;
    int[] IDs = new int[5];
}

public class UserSolution_24992_OTT {
    static final int MAX_GENRE = 5;
    static final int MAX_USERS = 1000;

    // 영화 ID <-> 내부 idx 매핑
    static Map<Integer, Integer> idToIdx = new HashMap<>();
    static Map<Integer, Integer> idxToId = new HashMap<>();
    static Movie[] movies = new Movie[10005];
    static int mIdx;

    // 장르별 영화 세트 (0번은 전체 영화 저장용)
    // int[]: {총점, 영화idx}
    static TreeSet<int[]>[] genreToMovies = new TreeSet[MAX_GENRE + 1];
    // 사용자별 시청 기록 (최신순으로 저장)
    // int[]: {총점, 영화idx}
    static List<LinkedList<int[]>> userToMovie = new ArrayList<>();

    // TreeSet 정렬 기준: 총점 내림차순, 같다면 최근 등록 순
    static Comparator<int[]> movieComparator = (a, b) -> {
        if (a[0] != b[0]) return Integer.compare(b[0], a[0]); // 총점 내림차순
        return Integer.compare(b[1], a[1]); // 더 나중에 등록된 영화 우선
    };

    public static void init(int N) {
    	// 장르별 영화 TreeSet 초기화
        for (int i = 0; i <= MAX_GENRE; i++) {
            genreToMovies[i] = new TreeSet<>(movieComparator);
        }
        // 사용자별 시청 기록 초기화
        userToMovie.clear();
        for (int i = 0; i <= N; i++) {
            userToMovie.add(new LinkedList<>());
        }
     // 영화 인덱스 관리 초기화
        idToIdx.clear();
        idxToId.clear();
        mIdx = 0;
    }

    // 영화 추가
    public static int add(int mID, int mGenre, int mTotal) {
        if (idToIdx.containsKey(mID)) return 0; // 이미 존재하면 실패
        int curIdx = mIdx;
        idToIdx.put(mID, curIdx);
        idxToId.put(curIdx, mID);

        // 영화 객체 생성
        movies[curIdx] = new Movie(mID, mGenre, mTotal);

        // 장르 및 전체 TreeSet에 삽입
        genreToMovies[mGenre].add(new int[]{mTotal, curIdx});
        genreToMovies[0].add(new int[]{mTotal, curIdx});

        mIdx++;
        return 1;
    }

    // 영화 삭제
    public static int erase(int mID) {
        if (!idToIdx.containsKey(mID)) return 0; // 존재하지 않으면 실패

        int curIdx = idToIdx.get(mID);
        movies[curIdx].removed = true; // 삭제 처리
        int curGenre = movies[curIdx].mGenre;
        int curTotal = movies[curIdx].mTotal;

        // TreeSet에서 제거
        genreToMovies[curGenre].remove(new int[]{curTotal, curIdx});
        genreToMovies[0].remove(new int[]{curTotal, curIdx});

        idToIdx.remove(mID); // 매핑 제거
        return 1;
    }

    // 시청
    public static int watch(int uID, int mID, int mRating) {
        if (!idToIdx.containsKey(mID)) return 0; // 영화 없음
        int curIdx = idToIdx.get(mID);
        Movie mv = movies[curIdx];

        if (mv.watchedUsers.contains(uID)) return 0; // 이미 시청한 경우 실패

        int curGenre = mv.mGenre;
        int curTotal = mv.mTotal;

        // 사용자 시청 기록에 "앞쪽"에 추가 (최근 시청이 앞)
        userToMovie.get(uID).addFirst(new int[]{curIdx, mRating});

        // 총점 업데이트 (TreeSet 갱신 필요 → 삭제 후 다시 삽입)
        genreToMovies[curGenre].remove(new int[]{curTotal, curIdx});
        genreToMovies[0].remove(new int[]{curTotal, curIdx});
        mv.mTotal += mRating;
        genreToMovies[curGenre].add(new int[]{mv.mTotal, curIdx});
        genreToMovies[0].add(new int[]{mv.mTotal, curIdx});

        mv.watchedUsers.add(uID); // 시청 기록 추가
        return 1;
    }

    // 추천
    public static RESULT suggest(int uID) {
        RESULT res = new RESULT();
        int maxRating = 0;   // 최근 본 영화 중 최고 평점
        int maxGenre = 0;    // 그 영화의 장르
        int cnt = 0;

        // 최근 시청 영화 5개 확인
        Iterator<int[]> it = userToMovie.get(uID).iterator();
        while (it.hasNext() && cnt < 5) {
            int[] entry = it.next();
            int tempIdx = entry[0];
            int tempRating = entry[1];

            if (movies[tempIdx].removed) {
                // 영화가 삭제되었으면 기록에서도 제거
                it.remove();
                continue;
            } else {
                // 가장 높은 평점을 가진 영화의 장르 선택
                if (maxRating < tempRating) {
                    maxRating = tempRating;
                    maxGenre = movies[tempIdx].mGenre;
                }
                cnt++;
            }
        }

        // 선택된 장르에서 추천 후보 탐색
        res.cnt = 0;
        for (int[] entry : genreToMovies[maxGenre]) {
            int tempIdx = entry[1];
            int tempID = idxToId.get(tempIdx);

            // 이미 시청한 영화는 제외
            if (movies[tempIdx].watchedUsers.contains(uID)) continue;

            res.IDs[res.cnt++] = tempID; // 추천 목록에 추가
            if (res.cnt >= 5) break;     // 최대 5개까지만
        }
        return res;
    }
}
