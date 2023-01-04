#include <iostream>
#include <vector>
using namespace std;

int main() {
	int n, m;
	cin >> n >> m;
	vector<int> b(n);
	while(m--) {
		int x, y, p;
		cin >> x >> y >> p;
		b[x] += p, b[y] -= p;
	}
	vector<int> dp(1 << n);
	for(int i = 1; i < 1 << n; ++i) {
		int balance = 0, best = 1e9;
		for(int j               = 0; j < n; ++j)
			if(i & 1 << j) best = min(best, dp[i ^ 1 << j]), balance += b[j];
		dp[i]                   = best + (balance != 0);
	}
	cout << dp[(1 << n) - 1] << endl;
	return 0;
}
