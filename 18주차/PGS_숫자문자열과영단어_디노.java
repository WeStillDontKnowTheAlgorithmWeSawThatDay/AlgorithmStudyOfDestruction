import java.util.*;
class Solution {
    public int solution(String s) {
        int answer = 0;

        while(s.length() != 0) {
            if (s.startsWith("zero")) {
                answer = answer * 10 + 0;
                s = s.substring(4, s.length());
                continue;
            }
            if (s.startsWith("one")) {
                answer = answer * 10 + 1;
                s = s.substring(3, s.length());
                continue;
            }
            if (s.startsWith("two")) {
                answer = answer * 10 + 2;
                s = s.substring(3, s.length());
                continue;
            }
            if (s.startsWith("three")) {
                answer = answer * 10 + 3;
                s = s.substring(5, s.length());
                continue;
            }
            if (s.startsWith("four")) {
                answer = answer * 10 + 4;
                s = s.substring(4, s.length());
                continue;
            }
            if (s.startsWith("five")) {
                answer = answer * 10 + 5;
                s = s.substring(4, s.length());
                continue;
            }
            if (s.startsWith("six")) {
                answer = answer * 10 + 6;
                s = s.substring(3, s.length());
                continue;
            }
            if (s.startsWith("seven")) {
                answer = answer * 10 + 7;
                s = s.substring(5, s.length());
                continue;
            }
            if (s.startsWith("eight")) {
                answer = answer * 10 + 8;
                s = s.substring(5, s.length());
                continue;
            }
            if (s.startsWith("nine")) {
                answer = answer * 10 + 9;
                s = s.substring(4, s.length());
                continue;
            }
            answer = answer * 10 + Integer.parseInt(s.substring(0, 1));
            s = s.substring(1, s.length());
        }

        return answer;
    }
}
