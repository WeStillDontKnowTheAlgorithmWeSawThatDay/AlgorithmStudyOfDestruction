import java.util.*;

class Solution {
    public long[] solution(long[] numbers) {
        long[] answer = new long[numbers.length];
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 4 == 3) {
                answer[i] = change(numbers[i]);
            } else {
                answer[i] = numbers[i] + 1;
            }
        }

        return answer;
    }

    public long change(long numbers) {

        long total = 0;
        String temp = "";
        boolean flag = false;

        while (numbers != 0) {
            if (numbers % 2 == 0) {
                temp += '0';
                flag = true;
            } else {
                temp += '1';
            }
            numbers /= 2;
        }
        if (flag == false) {
            temp += '0';
        }
        temp = temp.replaceFirst("10", "01");


        for (int i = 0; i < temp.length(); i++) {
            if (temp.charAt(i) == '1') {
                total += (long) Math.pow(2, i);
            }
        }

        return total;
    }
}
