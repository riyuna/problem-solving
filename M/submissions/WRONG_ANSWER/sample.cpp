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

	constexpr int ATTEMPTS = 300;
	vector<int> ans(E.size(), 1);
	for (int i = 0; i < (int)E.size(); ++i) {
		for (int j = max(0, i - ATTEMPTS); j < i; ++j)
			if (E[j].second <= E[i].second)
				ans[i] = max(ans[i], 1 + ans[j]);
		if (i - ATTEMPTS > 0)
			for (int r = ATTEMPTS; --r;) {
				int j = rand() % (i - ATTEMPTS);
				if (E[j].second <= E[i].second)
					ans[i] = max(ans[i], 1 + ans[j]);
			}
	}

	ans.push_back(0);

	cout << (*max_element(ans.begin(), ans.end())) << endl;
	return 0;
}

