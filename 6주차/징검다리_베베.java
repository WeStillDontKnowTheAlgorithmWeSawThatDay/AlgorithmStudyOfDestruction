import java.util.Arrays;

public class Solution {
    public int solution(int distance, int[] rocks, int n) {
        int answer = 0;

        Arrays.sort(rocks);

        int left = 1;
        int right = distance;

        while (left <= right) {
            int mid = (left + right) / 2;
            int removedRock = 0;
            int before = 0;

            for (int rock : rocks) {
                if (rock - before < mid) {
                    removedRock++;
                    continue;
                }

                before = rock;
            }

            if (distance - before < mid) {
                removedRock++;
            }

            if (removedRock > n) {
                right = mid - 1;
                continue;
            }

            answer = Math.max(answer, mid);
            left = mid + 1;
        }

        return answer;
    }
}
