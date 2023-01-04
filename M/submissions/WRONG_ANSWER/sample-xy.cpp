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

	vector<size_t> byx(E.size(), 0), byy(E.size(), 0),
		ibyx(E.size(), 0), ibyy(E.size(), 0);
	for (size_t i = 0; i < E.size(); ++i)
		byx[i] = byy[i] = i;
	sort(byx.begin(), byx.end(),
		[&E](const size_t &l, const size_t &r) {
			return E[l] < E[r];
	});
	sort(byy.begin(), byy.end(),
		[&E](const size_t &l, const size_t &r) {
			return make_pair(E[l].second, E[l].first) < make_pair(E[r].second, E[r].first);
	});
	for (size_t i = 0; i < E.size(); ++i)
		ibyx[byx[i]] = ibyy[byy[i]] = i;

	constexpr int ATTEMPTS = 50;
	vector<int> ans(E.size(), 1);
	for (size_t i : byx) {
		// BY X
		for (int j = max(0, int(ibyx[i]) - ATTEMPTS); j < ibyx[i]; ++j)
			if (E[byx[j]].second <= E[i].second)
				ans[i] = max(ans[i], 1 + ans[byx[j]]);
		if (int(ibyx[i]) - ATTEMPTS > 0)
			for (int r = ATTEMPTS; --r;) {
				int j = rand() % (ibyx[i] - ATTEMPTS);
				if (E[byx[j]].second <= E[i].second)
					ans[i] = max(ans[i], 1 + ans[byx[j]]);
			}
		// BY Y
		for (int j = max(0, int(ibyy[i]) - ATTEMPTS); j < ibyy[i]; ++j)
			if (E[byy[j]].first <= E[i].first)
				ans[i] = max(ans[i], 1 + ans[byy[j]]);
		if (int(ibyy[i]) - ATTEMPTS > 0)
			for (int r = ATTEMPTS; --r;) {
				int j = rand() % (ibyy[i] - ATTEMPTS);
				if (E[byy[j]].first <= E[i].first)
					ans[i] = max(ans[i], 1 + ans[byy[j]]);
			}
	}


	ans.push_back(0);

	cout << (*max_element(ans.begin(), ans.end())) << endl;
	return 0;
}

