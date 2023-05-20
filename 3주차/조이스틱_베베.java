class Solution {
    public int solution(String name) {
        int answer = 0;
        int length = name.length();

        for (char c : name.toCharArray()) {
            int count = c - 'A';
            answer += Math.min(count, 26 - count);
        }

        int minMove = length - 1;
        for (int i = 0; i < length; i++) {
            int next = i + 1;
            while (next < length && name.charAt(next) == 'A')
                next++;

            int move = i + length - next + Math.min(i, length - next);
            minMove = Math.min(minMove, move);
        }

        answer += minMove;

        return answer;
    }
}
