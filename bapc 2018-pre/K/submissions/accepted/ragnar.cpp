#include <iostream>
#include <tuple>
#include <vector>
using namespace std;
constexpr int M = 1e6;
struct K {
  long long advertised, actual;
};
struct P {
  vector<K> sizes;
};
struct A {
  K k;
  int i;
};
bool operator<(const A &l, const A &r) {
  return make_tuple(l.k.advertised, -l.k.actual) <
         make_tuple(r.k.advertised, -r.k.actual);
}
int main() {
  int B, k;
  cin >> B >> k;
  vector<P> ps(k);
  for (auto &p : ps) {
    int l;
    cin >> l;
    p.sizes.resize(l);
    for (auto &x : p.sizes) cin >> x.advertised;
  }
  for (auto &x : ps[0].sizes) x.actual = x.advertised;
  for (int j = 0; j < k - 1; ++j) {
    vector<long long> dp(M + 1, 1e18);  // Minimal actual # bolts
    dp[0] = 0;
    for (int i = 0, y; i <= M; ++i)
      if (dp[i] < 1e18)
        for (auto x : ps[j].sizes)
          if ((y = i + x.advertised) <= M) dp[y] = min(dp[y], dp[i] + x.actual);
    for (int i = M - 1; i > 0; --i)
      if (dp[i] == 1e18) dp[i] = dp[i + 1];
    for (auto &x : ps[j + 1].sizes) x.actual = dp[x.advertised];
  }
  A ans{{(long long)(1e18), (long long)(-1e18)},
        -1};  // min adv size/max actual size.
  for (int i = 0; i < k; ++i)
    for (auto &x : ps[i].sizes)
      if (x.actual >= B) ans = min(ans, {{x.advertised, -x.actual}, i});

  if (ans.i == -1) cout << "impossible" << endl;
  else cout << ans.k.advertised << endl;
}
