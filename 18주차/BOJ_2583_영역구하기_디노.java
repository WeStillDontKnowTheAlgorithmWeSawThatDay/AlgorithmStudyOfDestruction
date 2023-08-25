package org.example;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class BOJ_2538_영역구하기_디노 {
    static int M;
    static int N;
    static int K;

    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static boolean isPossible(int x, int y, int m, int n) {
        return 0 <= x && x < m && 0 <= y && y < n;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        M = sc.nextInt();
        N = sc.nextInt();
        K = sc.nextInt();

        int[][] arr = new int[M][N];

        for (int i = 0; i < K; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();

            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            for (int a = y1; a < y2; a++) {
                for (int b = x1; b < x2; b++) {
                    arr[a][b] = 1;
                }
            }
        }

        int ansCnt = 0;
        List<Integer> ansList = new ArrayList<>();

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if (arr[i][j] == 0) {
                    ansCnt++;
                    int cnt = 1;
                    Deque<List<Integer>> dq = new LinkedList<>();
                    dq.add(List.of(i, j));
                    arr[i][j] = 1;
                    while (!dq.isEmpty()) {
                        List<Integer> tmp = dq.pollFirst();
                        int x = tmp.get(0);
                        int y = tmp.get(1);
                        for (int d = 0; d < 4; d++) {
                            int nx = x + dx[d];
                            int ny = y + dy[d];

                            if (isPossible(nx, ny, M, N) && arr[nx][ny] == 0) {
                                dq.add(List.of(nx, ny));
                                arr[nx][ny] = 1;
                                cnt++;
                            }
                        }
                    }
                    ansList.add(cnt);
                }
            }
        }

        Collections.sort(ansList);
        System.out.println(ansCnt);
        for (Integer ans : ansList) {
            System.out.print(ans + " ");
        }
    }
}
