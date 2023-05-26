public class Solution {
    public boolean solution(String s) {
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) < 48 || 57 < s.charAt(i)) return false;
        }

        return 4 == s.length() || s.length() == 6;
    }
}
