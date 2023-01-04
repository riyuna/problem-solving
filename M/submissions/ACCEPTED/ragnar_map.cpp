#include <algorithm>
#include <cassert>
#include <cmath>
#include <iostream>
#include <limits>
#include <map>
#include <vector>
using namespace std;

struct increasing_function {
	using T = int;
	std::map<T, T> m;
	increasing_function() {
		m.insert({std::numeric_limits<int>::min(), numeric_limits<int>::min()});
	}

	void set(T x, T y) {
		auto next = m.upper_bound(x), p = prev(next);
		if(p->second < y) {
			if(p->first == x)
				p->second = y;
			else
				m.insert(next, {x, y});
			while(next != m.end() && next->second <= y) next = m.erase(next);
		}
	}
	T get(T x) {
		auto next = m.upper_bound(x);
		assert(next != m.begin());
		return prev(next)->second;
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

	increasing_function f;
	f.set(home.y, 0);
	for(auto &p : ps) f.set(p.y, f.get(p.y) + 1);
	cout << f.get(work.y) << endl;
}
