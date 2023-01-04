#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ii = pair<long, long>;
using vi = vector<ll>;
using vvi = vector<vi>;
using vii = vector<ii>;
using vvii = vector<vii>;

constexpr int BMAX = 2001;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	ll B;
	int K;
	cin >> B >> K;

	vvii prices(K);
	for (int i = 0; i < K; ++i) {
		vi dp(BMAX+1, -1LL);
		dp[0] = 0LL;

		if (i > 0) {
			for (ii price : prices[i-1]) {
				ll sticker, real;
				tie(sticker, real) = price;
				for (int j = 0; j <= BMAX - sticker; ++j) {
					if (dp[j] >= 0LL) {
						ll new_real = dp[j] + real;
						if (dp[j+sticker] > new_real || dp[j+sticker] < 0)
							dp[j+sticker] = new_real;
					}
				}
			}
		}

		int L, N;
		cin >> L;
		while (L--) {
			cin >> N;
			if (i == 0)
				prices[i].push_back({N, N});
			else {
				for (int j = N; j <= BMAX; ++j)
					if (dp[j] >= 0LL) {
						prices[i].push_back({N, dp[j]});
						break;
					}
			}
		}
	}

	ll ans = -1LL;
	for (int i = 0; i < K; ++i)
		for (ii price : prices[i])
			if (price.second >= B)
				ans = (ans < 0LL || ans > price.first ? price.first : ans);
	if (ans == -1LL) cout << "impossible" << endl;
	else cout << ans << endl;
}
