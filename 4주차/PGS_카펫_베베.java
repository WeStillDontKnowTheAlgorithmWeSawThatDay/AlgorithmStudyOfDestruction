public class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        int s = brown + yellow;

        for (int i = 3; i < s; i++) {

            if (s % i == 0 && s / i >= 3) {
                int height = Math.max(i, s / i);
                int width = Math.min(i, s / i);
                int center = (height - 2) * (width - 2);

                if (center == yellow) {
                    answer[0] = height;
                    answer[1] = width;
                    return answer;
                }
            }
        }
        return answer;
    }
}
