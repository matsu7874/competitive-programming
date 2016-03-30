#include <bits/stdc++.h>
// #include <cstdio>
using namespace std;

int main() {
  int w, h;

  scanf("%d %d", &w, &h);
  printf("%d %d\n", w, h);

  long p[10001][10001];

  for (int i = 0; i < h; ++i) {
    for (int j = 0; j < w; ++j) {
      p[i][j] = 0;
    }
  }
  p[0][0] = 1;

  // for (int i = 0; i < h - 1; ++i) {
  //   for (int j = 0; j < w - 1; ++j) {
  //     p[i][j]     %= 1000000007;
  //     p[i][j + 1] += p[i][j];
  //     p[i + 1][j] += p[i][j];
  //   }
  // }
  //
  // for (int i = 0; i < h - 1; ++i) {
  //   p[i + 1][w - 1] = (p[i + 1][w - 1] + p[i][w - 1]) % 1000000007;
  // }
  //
  // for (int i = 0; i < w - 1; ++i) {
  //   p[h - 1][i + 1] = (p[h - 1][i + 1] + p[h - 1][i]) % 1000000007;
  // }
  printf("%ld\n", p[h-1][w-1]);
  return 0;
}
