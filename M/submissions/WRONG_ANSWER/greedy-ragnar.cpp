#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <map>
#include <vector>
using namespace std;

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

	bool toggle_y = false;
	if(home.y > work.y) {
		toggle_y = true;
		// flip the sign of all y coords so that home.y <= work.y
		home.y = -home.y;
		work.y = -work.y;
	}

	std::vector<P> ps;
	ps.reserve(n);
	while(n--) {
		P p;
		cin >> p;
		if(toggle_y) p.y = -p.y;
		if(!(home.x <= p.x && p.x <= work.x)) continue;
		// optionally, filter y as well
		// if(!(home.y <= p.y && p.y <= work.y)) continue;
		ps.push_back(p);
	}

	std::sort(ps.begin(), ps.end());
	int ans = 0;
	int y   = home.y;
	for(auto &p : ps)
		if(p.y >= y) y = p.y, ++ans;
	cout << ans << endl;
}
