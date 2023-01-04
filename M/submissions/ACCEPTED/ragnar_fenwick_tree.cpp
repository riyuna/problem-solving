#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <map>
#include <vector>
using namespace std;
using T = int;
struct FenwickTree { // queries are right-exclusive; 0-based
	int n;
	vector<T> tree;
	FenwickTree(int n) : n(n) { tree.assign(n + 1, 0); }
	T query(int l, int r) { return query(r) - query(l); } // [l,r)
	T query(int r) {                                      // [0,r)
		T s                             = 0;
		for(; r > 0; r -= (r & (-r))) s = max(s, tree[r]);
		return s;
	}
	void update(int i, T v) {
		for(++i; i <= n; i += (i & (-i))) tree[i] = max(tree[i], v);
	}
};

// the grid is on even rows/cols
struct P {
	int x, y;
	friend istream &operator>>(istream &i, P &p) { return i >> p.x >> p.y; }
	friend bool operator<(const P &l, const P &r) { return l.x != r.x ? l.x < r.x : l.y < r.y; }
};

int main() {
	int n;
	cin >> n;
	P home, work;
	cin >> home >> work;

	if(work.x < home.x) swap(home, work);
	// now: home.x <= work.x

	// for coordinate compression
	map<int, int> ys;

	bool toggle_y = false;
	if(home.y > work.y) {
		toggle_y = true;
		// flip the sign of all y coords so that home.y <= work.y
		home.y = -home.y;
		work.y = -work.y;
	}

	ys[home.y];
	ys[work.y];

	std::vector<P> ps;
	ps.reserve(n);
	while(n--) {
		P p;
		cin >> p;
		if(toggle_y) p.y = -p.y;
		if(!(home.x <= p.x && p.x <= work.x)) continue;
		// optionally, filter y as well
		if(!(home.y <= p.y && p.y <= work.y)) continue;
		ps.push_back(p);
		ys[p.y];
	}

	// apply compression
	int lasty                    = 0;
	for(auto &yy : ys) yy.second = lasty++;
	home.y                       = ys[home.y];
	work.y                       = ys[work.y];
	for(auto &p : ps) p.y        = ys[p.y];

	std::sort(ps.begin(), ps.end());

	FenwickTree f(lasty);
	for(auto &p : ps) f.update(p.y, f.query(p.y + 1) + 1);
	cout << f.query(work.y + 1) << endl;
}
