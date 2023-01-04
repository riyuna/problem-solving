// Solution of Raymond van Bommel
// Problem: Bills

#include <iostream>

using namespace std;

long long balance[20];
bool zerosubset[1048576];
int longestchain[1048576];
int M, N;

void findsubsets (int i, int currsum, int subsetnr) {
	if (i == M) {
		
		//cerr << "subsetnr = " << subsetnr << '\n';
		//cerr << "currsum = " << currsum << '\n';
		
		longestchain[subsetnr] = -1;
		if (currsum == 0)
			zerosubset[subsetnr] = true;
		else
			zerosubset[subsetnr] = false;
		return;
	}
	findsubsets(i+1, currsum, 2*subsetnr);
	findsubsets(i+1, currsum+balance[i], 2*subsetnr+1);
	return;
}

int main () {
	cin >> M >> N;
	long long totalsubsets = (1LL << M);
	//cerr << totalsubsets << '\n';
	for (int i = 0; i < N; i++) {
		int a, b;
		long long p;
		cin >> a >> b >> p;
		balance[a] += p;
		balance[b] -= p;
	}
	findsubsets(0,0,0);
	for (int i = 0; i < totalsubsets; i++) {
		for (int j = 1; j <= i; j *= 2) {
			if ((i & j) > 0) {
				longestchain[i] = max(longestchain[i], longestchain[i-j]);
				//cerr << "longestchain[" << i << "] = max(..., longestchain[" << i-j << "] + 1) = "<< longestchain[i] << "\n";
			}
		}
		if (zerosubset[i])
			longestchain[i]++;
	}
	cout << M - longestchain[totalsubsets-1] << '\n';
	return 0;
}
