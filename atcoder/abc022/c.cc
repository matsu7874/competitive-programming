// g++ -std=c++0x -O2
#include <bits/stdc++.h>
using namespace std;

int main() {
  int n, m, u, v, l;

  scanf("%d %d", &n, &m);

  long long dist[300][300];

  for (int i = 0; i < n; ++i) {
    for (int j = 0; j < n; ++j) {
      dist[i][j] = INT_MAX;
    }
  }

  for (int i = 0; i < m; ++i) {
    scanf("%d %d %d", &u, &v, &l);
    --u;
    --v;
    dist[u][v] = l;
    dist[v][u] = l;
  }

  for (int k = 1; k < n; ++k) {
    for (int i = 1; i < n; ++i) {
      for (int j = 1; j < n; ++j) {
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
      }
    }
  }
  long long ans = INT_MAX;

  for (int i = 1; i < n; ++i) {
    for (int j = i + 1; j < n; ++j) {
      ans = min(ans, dist[0][i] + dist[i][j] + dist[j][0]);
    }
  }

  if (ans == INT_MAX) {
    printf("-1\n");
  } else {
    printf("%lld\n", ans);
  }
  return 0;
}
