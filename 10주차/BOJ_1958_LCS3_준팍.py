import sys

input = sys.stdin.readline

str1, str2, str3 = input().strip(), input().strip(), input().strip()
len1, len2, len3 = len(str1), len(str2), len(str3)

# 3차원 점화식 만들기
dp = [[[0] * (len3+1) for _ in range(len2+1)] for __ in range(len1+1)]
    
for i in range(1, len1+1):
    for j in range(1, len2+1):
         for k in range(1, len3+1):
            # 문자열이 같을 시, 이전 점화식 결과에 1을 더한 값을 저장한다.
            if str1[i-1] == str2[j-1] == str3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            # 문자열이 다를 시, 이전 점화식 중 가장 큰 값을 저장한다. 
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
                    
# LCS의 길이 출력
print(dp[-1][-1][-1])
