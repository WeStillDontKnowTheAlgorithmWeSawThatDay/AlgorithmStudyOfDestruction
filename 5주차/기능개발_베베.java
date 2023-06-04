import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int[] progressesArgs, int[] speedsArgs) {
        List<Integer> progresses = new ArrayList<>();
        for (int i = 0; i < progressesArgs.length; i++) {
            progresses.add(progressesArgs[i]);
        }

        List<Integer> releaseDates = new ArrayList<>();

        while (!progresses.isEmpty()) {
            int cnt = 0;

            while (!progresses.isEmpty() && progresses.get(0) >= 100) {
                progresses.remove(0);
                speedsArgs = removeElement(speedsArgs, 0);
                cnt++;
            }

            if (cnt > 0) {
                releaseDates.add(cnt);
            }

            for (int i = 0; i < progresses.size(); i++) {
                progresses.set(i, progresses.get(i) + speedsArgs[i]);
            }
        }

        int[] results = new int[releaseDates.size()];
        for (int i = 0; i < releaseDates.size(); i++) {
            results[i] = releaseDates.get(i);
        }

        return results;
    }

    private int[] removeElement(int[] arr, int index) {
        int[] newArr = new int[arr.length - 1];
        System.arraycopy(arr, 0, newArr, 0, index);
        System.arraycopy(arr, index + 1, newArr, index, arr.length - index - 1);
        return newArr;
    }
}
