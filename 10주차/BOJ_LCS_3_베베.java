import java.io.*;
import java.util.*;

public class n01958 {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String a = br.readLine();
        String b = br.readLine();
        String c = br.readLine();

        int len = getLCS(a, b, c);

        bw.write(len + "\n");
        bw.flush();

    }

    public static int getLCS(String a, String b, String c) {

        int[][][] dp = new int[a.length() + 1][b.length() + 1][c.length() + 1];

        for (int i = 1; i <= a.length(); i++) {
            char ch1 = a.charAt(i - 1);

            for (int j = 1; j <= b.length(); j++) {
                char ch2 = b.charAt(j - 1);

                for (int k = 1; k <= c.length(); k++) {
                    char ch3 = c.charAt(k - 1);

                    if (ch1 == ch2 && ch2 == ch3)
                        dp[i][j][k] = dp[i - 1][j - 1][k - 1] + 1;

                    else
                        dp[i][j][k] = Math.max(dp[i - 1][j][k], Math.max(dp[i][j - 1][k], dp[i][j][k - 1]));

                }
            }
        }

        return dp[a.length()][b.length()][c.length()];

    }

}
