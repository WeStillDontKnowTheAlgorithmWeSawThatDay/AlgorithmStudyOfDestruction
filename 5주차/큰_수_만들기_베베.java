import java.util.Stack;

class Solution {
    public String solution(String number, int k) {
        int len = number.length();
        int pick = len - k;

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < len; i++) {
            char ch = number.charAt(i);

            while (!stack.isEmpty() && stack.peek() < ch && k > 0) {
                stack.pop();
                k--;
            }

            stack.push(ch);
        }

        while (stack.size() > pick) {
            stack.pop();
        }

        StringBuilder answer = new StringBuilder();
        while (!stack.isEmpty()) {
            answer.insert(0, stack.pop());
        }

        return answer.toString();
    }
}
