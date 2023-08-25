class Solution {
    public int[] solution(String s) {
        // int[] answer = {};
        int parseCnt = 0;
        int zeroCnt = 0;

        while(!s.equals("1")) {
            int i = 0;
            parseCnt++;
            while(i < s.length()) {
                // System.out.println(s.charAt(i));
                if(s.charAt(i) == '0') {
                    zeroCnt++;
                    s = s.substring(0, i) + s.substring(i+1, s.length());
                    continue;
                }
                i++;
            }
            int c = s.length();
            // System.out.println(c);
            // System.out.println(Integer.toBinaryString(c));
            s = Integer.toBinaryString(c);

            // System.out.println(s);

        }
        int[] answer = {parseCnt, zeroCnt};


        return answer;
    }
}