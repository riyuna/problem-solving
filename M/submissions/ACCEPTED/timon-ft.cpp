#include <bits/stdc++.h>
using namespace std;

template <class T>
struct FenwickTree { // queries are right-exclusive; 0-based
	int n;
	vector<T> tree;
	FenwickTree(int n) : n(n) { tree.assign(n + 1, 0); }
	T query(int l, int r) { return query(r) - query(l); } // [l,r)
	T query(int r) {                                      // [0,r)
		T s = 0;
		for(; r > 0; r -= (r & (-r))) s = max(s, tree[r]);
		return s;
	}
	void update(int i, T v) {
		for(++i; i <= n; i += (i & (-i))) tree[i] = max(tree[i], v);
	}
};

int main() {
	int n, xm, ym, xM, yM;
	cin >> n >> xm >> ym >> xM >> yM;

	if (xm > xM) swap(xm, xM), swap(ym, yM);
	int m = ym <= yM ? 1 : -1;
	ym *= m;
	yM *= m;

	vector<pair<int, int>> E;
	map<int, int> xc, yc;
	for (int i = 0; i < n; ++i) {
		int x, y;
		cin >> x >> y;
		y *= m;
		if (x < xm || x > xM || y < ym || y > yM) continue;
		E.push_back({x, y});
		xc[x] = yc[y] = 0;
	}

	int cx = 0, cy = 0;
	for (auto &it : xc) it.second = cx++;
	for (auto &it : yc) it.second = cy++;
	for (auto &it : E) it = {xc[it.first], yc[it.second]};

	sort(E.begin(), E.end());
	FenwickTree<int> ft(cy);
	for (auto xy : E) {
		ft.update(xy.second, ft.query(xy.second+1)+1);
	}

	cout << ft.query(cy) << endl;

	return 0;
}

