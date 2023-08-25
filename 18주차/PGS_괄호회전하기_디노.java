import java.util.*;
class Solution {

    public boolean check(String word) {
        Stack<Character> stack = new Stack<>();
        for(int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if(stack.isEmpty()) {
                stack.push(c);
                continue;
            }
            if(c == ')' && stack.peek().equals('(')) {
                stack.pop();
                continue;
            }
            if(c == '}' && stack.peek().equals('{')) {
                stack.pop();
                continue;
            }
            if(c == ']' && stack.peek().equals('[')) {
                stack.pop();
                continue;
            }
            stack.push(c);
        }
        return stack.isEmpty();
    }

    public int solution(String s) {
        int answer = 0;

        for(int i = 0; i < s.length(); i++) {
            String tmp = s.substring(i, s.length()) + s.substring(0, i);
            if (check(tmp)) {
                answer += 1;
            }
        }
        return answer;
    }
}