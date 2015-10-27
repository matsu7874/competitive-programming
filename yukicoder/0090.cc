#include <bits/stdc++.h>

using namespace std;

int main() {
  int N, M;

  scanf("%d %d", &N, &M);

  vector<vector<int> > score = vector<vector<int> >(9, vector<int>(9, 0));

  for (int i = 0; i < M; i++) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    score[a][b] = c;
  }
  long long int max_score = 0;
  int p[10];

  for (int i = 0; i < N; i++) {
    p[i] = i;
  }

  do {
    int s = 0;

    for (int i = 0; i < N - 1; i++)
      for (int j = i + 1; j < N; j++) s += score[p[i]][p[j]];
    if (s > max_score) max_score = s;
  } while (next_permutation(p, p + N));
  printf("%d\n", max_score);
  return 0;
}
