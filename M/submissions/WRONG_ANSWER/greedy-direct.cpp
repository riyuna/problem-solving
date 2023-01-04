#include <bits/stdc++.h>
using namespace std;

int main() {
	int n, xm, ym, xM, yM;
	cin >> n >> xm >> ym >> xM >> yM;

	if (xm > xM) swap(xm, xM), swap(ym, yM);
	int m = ym <= yM ? 1 : -1;
	ym *= m;
	yM *= m;

	vector<pair<int, int>> E;
	for (int i = 0; i < n; ++i) {
		int x, y;
		cin >> x >> y;
		y *= m;
		if (x < xm || x > xM || y < ym || y > yM) continue;
		E.push_back({x, y});
	}
	sort(E.begin(), E.end());

	int ans = 0;
	map<int, int> mp{ make_pair(0, 0) };
	for (auto xy : E) {
		auto it = --mp.upper_bound(xy.second);
		int v = 1 + it->second;
		mp[xy.second] = v;
		ans = max(ans, v);
	}

	cout << ans << endl;
	return 0;
}

