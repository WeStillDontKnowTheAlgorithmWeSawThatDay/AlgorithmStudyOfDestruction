class Solution {
    public String solution(String s) {
        String answer = "";
        int cnt = 0;
        String[] strArr = s.split("");

        for (String s1 : strArr) {
            if(s1.contains(" ")){
                cnt = 0;
            } else {
                cnt++;
            }

            if(cnt%2 == 0) {
                answer += s1.toLowerCase();
            } else {
                answer += s1.toUpperCase();
            }
        }
        return answer;
    }
}