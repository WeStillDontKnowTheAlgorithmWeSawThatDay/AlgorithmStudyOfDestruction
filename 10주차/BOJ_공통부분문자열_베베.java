import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String cmp1 = br.readLine();
        String cmp2 = br.readLine();
        int len1 = cmp1.length();
        int len2 = cmp2.length();
        int max = 0;
        int[][] map = new int[len1 + 1][len2 + 1];
        for(int i = 1; i <= len1; i++) {
            for(int j = 1; j <= len2; j++) {
                if(cmp1.charAt(i-1) == cmp2.charAt(j-1)) {
                    map[i][j] = map[i-1][j-1] + 1;
                    max = Math.max(max, map[i][j]);
                }
            }
        }
        System.out.println(max);
    }
}
