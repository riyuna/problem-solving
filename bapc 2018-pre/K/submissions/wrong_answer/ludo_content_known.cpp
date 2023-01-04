#include <bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back
#define rep(i, a, b) for(auto i = (a); i != (b); ++i)
#define REP(i, n) rep(i, 0, n)
#define all(v) (v).begin(), (v).end()

typedef long long ll;

int B, K;
// (a, b) \in sizes[i]: company i has a package of size a, containing at least b bolts.
vector<pair<int, ll>> sizes[10];

const ll INF = 9e18;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> B >> K;
	REP(i, K) {
		int len;
		cin >> len;
		sizes[i].resize(len);
		while(len--) cin >> sizes[i][len].x;
		// sort ascendingly
		sort(all(sizes[i]));
	}

	int ret = 2147483647;
	// first company is easy:
	for(auto &pr : sizes[0]) {
		pr.y = pr.x;
		if(pr.y >= B) ret = min(ret, pr.x);
	}

	for(int i = 1; i < K; i++) {
		// perform knapsacks
		int msize = sizes[i].back().x;

		// A[i]: minimum amount of bolts that is inside a collection consisting
		// of i bolts from several packages of the previous company, or INF if
		// not possible to make this amount.
		// Take the minimum because it must always work independent of selection
		// by the companies' packaging system.
		vector<ll> A(msize * 2 + 1, INF);
		A[0] = 0;
		for(auto pr : sizes[i - 1]) {
			for(int j = 0; j + pr.x < (int)A.size(); j++)
				A[j + pr.x] = min(A[j + pr.x], A[j] + pr.y);
		}

		assert(sizes[i].size() > 0);

		int pkg = 0;
		for(int j = 0; pkg < (int)sizes[i].size() && j < (int)A.size(); ) {
			if(A[j] < INF && A[j] >= sizes[i][pkg].x) {
				// package this
				sizes[i][pkg].y = A[j];
				// cerr << "Package " << i << ", " << pkg << ": " << A[j] << endl;
				pkg++;
			} else j++;
		}

		// ASSUMPTION: for all j, sizes[i][j] is different
		for(int ppkg = 0; pkg < (int)sizes[i].size() && ppkg < (int)sizes[i - 1].size(); ) {
			if(sizes[i - 1][ppkg].x >= sizes[i][pkg].x) {
				sizes[i][pkg++].y = sizes[i - 1][ppkg].y;
			} else ppkg++;
		}

		assert(pkg == (int)sizes[i].size());

		for(auto pr : sizes[i]) {
			if(pr.y >= B) ret = min(ret, pr.x);
		}
	}

	if(ret == 2147483647)
		cout << "impossible" << endl;
	else
		cout << ret << endl;
	return 0;
}
