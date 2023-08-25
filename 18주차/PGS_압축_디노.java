import java.util.*;
class Solution {
    public int[] solution(String msg) {
        int[] answer = {};
        ArrayList<Integer> ans = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();

        int num = 1;
        for(int i = 'A'; i <= 'Z'; i++) {
            map.put(String.valueOf((char)i), num);
            num++;
        }
        // System.out.println(map.get('A'));

        int idx = 0;
        while(idx < msg.length()) {
            String word = "";
            while(idx < msg.length()) {
                if(map.containsKey(word + msg.charAt(idx))) {
                    word += msg.charAt(idx);
                    idx++;
                    continue;
                }
                break;
            }

            ans.add(map.get(word));
            if(idx < msg.length()) {
                map.put(word + msg.charAt(idx), num);
                num++;
            }
        }

        answer = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }
        return answer;
    }
}
