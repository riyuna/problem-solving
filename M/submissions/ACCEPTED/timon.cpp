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

	int c = 0;
	set<pair<int, int>> level;
	for (auto xy : E) {
		auto it = level.lower_bound({xy.second, int(1e9)});
		if (it != level.end())
			level.erase(it);
		level.insert({xy.second, c++});
	}

	cout << level.size() << endl;
	return 0;
}