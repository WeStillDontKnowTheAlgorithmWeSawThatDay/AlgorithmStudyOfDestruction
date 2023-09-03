package org.example;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_4811_알약_디노 {

    public static long cnt = 0;
    public static long dp[];
    public static int N;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        dp = new long[31];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;

        while (true) {
            N = Integer.parseInt(br.readLine());
            if (N == 0) {
                break;
            }
            for (int i = 3; i < 31; i++) {
                cnt = 0;
                for (int j = 0; j < i; j++) {
                    cnt += dp[j] * dp[i - 1 - j];
                }
                dp[i] = cnt;
            }
            System.out.println(dp[N]);
        }
    }
}
