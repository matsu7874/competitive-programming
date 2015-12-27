// g++ -std=c++0x -O2
#include <bits/stdc++.h>
using namespace std;

#define MAX_V 32768
int main() {
  int N;
  int A[5000];
  int  i, j;
  bool dp[MAX_V];

  scanf("%d", &N);

  for (i = 0; i < N; ++i) {
    scanf("%d", &A[i]);
  }

  for (i = 1; i < MAX_V; ++i) {
    dp[i] = false;
  }
  dp[0] = true;

  for (i = 0; i < N; ++i) {
    for (j = 0; j < MAX_V; ++j) {
      if (dp[j]) {
        dp[j ^ A[i]] = true;
      }
    }
  }
  int cnt = 0;

  for (i = 0; i < MAX_V; ++i) {
    if (dp[i]) {
      cnt += 1;
    }
  }
  printf("%d\n", cnt);
  return 0;
}
