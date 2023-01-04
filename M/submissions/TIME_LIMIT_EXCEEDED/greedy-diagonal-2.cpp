//@EXPECTED_RESULTS@: TIMELIMIT,WRONG_ANSWER
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
	bool operator==(const P &r) { return x == r.x && y == r.y; }
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
		if(!(home.y <= p.y && p.y <= work.y)) continue;
		ps.push_back(p);
	}

	// sort by x+y
	std::sort(ps.begin(), ps.end(), [](const P &l, const P &r) {
		int sl = l.x + l.y, sr = r.x + r.y;
		return sl != sr ? sl < sr : l.x < r.x;
	});
	map<P, int> front;
	front[{0, 0}] = 0;
	int ans = 0;
	for(auto p : ps) {
		auto it       = front.lower_bound({p.x, int(1e9 + 1)});
		int best      = 0;
		int countdown = 1e9;
		while(it != front.begin()) {
			if(--countdown == 0) break;
			--it;
			if(it->first.y > p.y) {
				countdown = min(countdown, 100);
				continue;
			}
			// assert(it->first.x <= p.x);
			best = max(best, it->second);
			// do some heuristic pruning
			// if(it->second < ans - 10000) it = front.erase(it);
		}
		++best;
		ans      = max(ans, best);
		front[p] = best;
	}
	cout << ans << endl;
}
