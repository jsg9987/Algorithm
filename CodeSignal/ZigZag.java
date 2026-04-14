int[] solution(int[] numbers) {
    int len = numbers.length;
    int[] result = new int[len - 2];

    int resultIdx = 0;
    for(int i = 1; i < len - 1; i++) {
        if((numbers[i-1] < numbers[i] && numbers[i] > numbers[i+1]) || (numbers[i-1] > numbers[i] && numbers[i] < numbers[i+1])) {
            result[resultIdx] = 1;
        } else {
            result[resultIdx] = 0;
        }

        resultIdx++;
    }

    return result;
}
