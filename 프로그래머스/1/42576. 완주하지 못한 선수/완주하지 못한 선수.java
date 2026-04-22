import java.io.*;
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        // participant, completion hashMap 생성해 사람들 숫자 카운트
        HashMap<String, Integer> participantMap = new HashMap<>();
        HashMap<String, Integer> completionMap = new HashMap<>();
        
        for(int i = 0; i < participant.length; i++) {
            // 없으면 만들고, 있으면 ++
            if(!participantMap.containsKey(participant[i])) {
                participantMap.put(participant[i], 1);
            } else {
                participantMap.put(participant[i], participantMap.get(participant[i]) + 1);
            }
        }
        
        for(int i = 0; i < completion.length; i++) {
            // 없으면 만들고, 있으면 ++
            if(!completionMap.containsKey(completion[i])) {
                completionMap.put(completion[i], 1);
            } else {
                completionMap.put(completion[i], completionMap.get(completion[i]) + 1);
            }
        }
        
        // 모든사람이 존재하는 participant 기준으로 없는사람 체크
        // 판별로직: value값이 다르거나? completion에는 없으면 해당인물
        for(int i = 0; i < participant.length; i++) {
            String name = participant[i];
            if(!participantMap.get(name).equals(completionMap.get(name)) || !completionMap.containsKey(name)) {
                return name;
            }
        }
        
        return "";
    }
}