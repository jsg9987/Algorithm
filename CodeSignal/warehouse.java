int solution(int[] centerCapacities, String[] dailyLog) {
    int capacityLen = centerCapacities.length;
    int dailyLogLen = dailyLog.length;

    int[] backup = new int[capacityLen];
    for(int i = 0; i < backup.length; i++) {
        backup[i] = centerCapacities[i];
    }

    boolean[] isClosed = new boolean[capacityLen];
    int[] resultArr = new int[capacityLen];
    int idx = 0;


    for(int i = 0; i < dailyLogLen; i++) {
        if(idx == (capacityLen - 1) && (centerCapacities[idx] <= 0 || isClosed[idx])) {
            idx = 0;
            for(int j = 0; j < capacityLen; j++) {
                centerCapacities[j] = backup[j];
            }
        }

        if(centerCapacities[idx] <= 0 || isClosed[idx]) {
            i--;
            idx++;
            continue;
        }
        String cur = dailyLog[i];
        String[] st = cur.split(" ");
        for(int j = 0; j < st.length; j++) {
            System.out.println(st[j]);
        }

        // PACKAGE면 처리할 수 있는지 확인
        if(st[0].equals("PACKAGE")) {
            if(!isClosed[idx] && centerCapacities[idx] > 0) {
                centerCapacities[idx]--;
                resultArr[idx]++;
            }
        } else { // 물류창고 Closing  처리
            int closingIdx = Integer.parseInt(st[1]);
            isClosed[closingIdx] = true;
        }
    }

    int maxIdx = 0;
    int maxValue = 0;
    for(int i = capacityLen - 1; i >= 0; i--) {
        if(resultArr[i] > maxValue) {
            maxValue = resultArr[i];
            maxIdx = i;
        }
    }

    return maxIdx;
}