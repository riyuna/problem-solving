#include<bits/stdc++.h>

using namespace std;

#define x first
#define y second
#define pb push_back
#define eb emplace_back
#define rep(i,a,b) for(auto i = (a); i != (b); ++i)
#define REP(i,n) rep(i,0,n)
#define all(v) (v).begin(), (v).end()

typedef long long ll;

int B, K;
vector< pair<int, ll> > sizes[10];

const ll INF = 9e18;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> B >> K;
	REP(i, K) {
		int len;
		cin >> len;
		sizes[i].resize(len);
		while (len--) cin >> sizes[i][len].x;
		// sort ascendingly
		sort(all(sizes[i]));
	}

	// first one is easy!
	for (auto &pr : sizes[0]) pr.y = pr.x;
	
	int ret = 2147483647;

	for (int i = 1; i < K; i++) {
		// perform knapsacks
		// knapsack
		int msize = 0;
		for(auto pr : sizes[i]) msize = max(msize, pr.x);

		// A[i]: minimum amount of bolts that is inside a collection consisting
		// of i bolts from several packages of the previous company, or INF if
		// not possible to make this amount.
		// Take the minimum because it must always work independent of selection
		// by the companies' packaging system.
		vector<ll> A(msize * 2 + 1, INF);
		A[0] = 0;
		for(auto pr : sizes[i - 1]) {
			for (int j = 0; j + pr.x < (int) A.size(); j++)
				A[j + pr.x] = min(A[j + pr.x], A[j] + pr.y);
		}

		int it = 0;
		for (int j = 0; j < (int) A.size() && it < (int) sizes[i].size(); ) {
			// WA: companies do not know how much bolts are actually inside...
			if (A[j] != INF && A[j] >= sizes[i][it].x) {
				// it fits
				sizes[i][it++].y = A[j];
			} else j++;
		}

		if (it < (int) sizes[i].size()) {
			// there were items bigger than msize before!
			int j = 0;
			while (it < (int) sizes[i].size() && j < (int) sizes[i - 1].size()) {
				if (sizes[i - 1][j].x >= sizes[i][it].x) {
					sizes[i][it++].y = sizes[i - 1][j].y;
				} else j++;
			}
		}
		assert(it == (int) sizes[i].size());

		for(auto pr : sizes[i]) {
			if (pr.y >= B)
				ret = min(ret, pr.x);
		}
	}

	if (ret == 2147483647)
		cout << "impossible" << endl;
	else
		cout << ret << endl;
	return 0;
}
