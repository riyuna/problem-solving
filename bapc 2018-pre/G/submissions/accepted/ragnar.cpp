#include <algorithm>
#include <array>
#include <cassert>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main() {
  array<int, 3> ts;
  for (auto &x : ts) cin >> x;
  int T = ts[0] + ts[1] + ts[2];
  int n;
  cin >> n;
  array<pair<int, int>, 3> o{{{-1, -1}, {-1, -1}, {-1, -1}}};
  vector<pair<int, int>> d;
  d.reserve(n);
  while (n--) {
    int t;
    string c;
    cin >> t >> c;
    t %= T;
    int id = 0;
    if (c == "green")
      id = 0;
    else if (c == "yellow")
      id = 1;
    else if (c == "red")
      id = 2;
    else
      assert(false);
    d.push_back({t, id});
    d.push_back({t + T, id});
  }
  sort(d.begin(), d.end());
  // Make sure all intervals are non-wrapping, and the times are increasing.
  int last_colour = d.back().second;

  for (int i = 0; i < d.size(); ++i) {
    int c = d[i].second;
    if (c != last_colour) {
      if (o[c].first != -1) break;
      o[c].first = d[i].first;
    }
    o[c].second = d[i].first;
    last_colour = c;
  }

  for (int i = 0; i <= 1; ++i) {
    if (o[i].first > o[i + 1].first) o[i + 1].first += T, o[i + 1].second += T;
  }

  // Find minimal valid offset.
  int t_min = max(o[0].second - ts[0],
                  max(o[1].second - ts[0] - ts[1], o[2].second - T));
  int t_max =
      min(o[0].first, min(o[1].first - ts[0], o[2].first - ts[0] - ts[1]));
  assert(t_min < t_max);

  // Answer query.
  int tq;
  string sq;
  cin >> tq >> sq;
  tq %= T;
  int i_min, i_max;
  if (sq == "green") {
    i_min = tq - ts[0];
    i_max = tq;
  } else if (sq == "yellow") {
    i_min = tq - ts[0] - ts[1];
    i_max = tq - ts[0];
  } else if (sq == "red") {
    i_min = tq - ts[0] - ts[1] - ts[2];
    i_max = tq - ts[0] - ts[1];
  } else
    assert(false);
  while (i_max > t_min) i_min -= T, i_max -= T;
  while (i_max <= t_min) i_min += T, i_max += T;
  int len = max(min(t_max, i_max) - max(t_min, i_min), 0);
  cout << setprecision(15) << double(len) / (t_max - t_min) << endl;
}
