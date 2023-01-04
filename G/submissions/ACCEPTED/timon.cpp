#include <bits/stdc++.h>
using namespace std;

int main() {
	int M, N;
	cin >> M >> N;
	vector<int> C(M, 0);
	while (N--) {
		int a, b, p;
		cin >> a >> b >> p;
		C[a] -= p;
		C[b] += p;
	}

	vector<int> dp(1<<M, 0);
	for (int m = 1; m < (1<<M); ++m) {
		int sum = 0;
		for (int i = 0; i < M; ++i)
			if ((m>>i)&1)
				sum += C[i],
				dp[m] = max(dp[m], dp[m&~(1<<i)]);
		if (sum == 0) ++dp[m];
	}

	cout << (M - dp.back()) << endl;
	return 0;
}
