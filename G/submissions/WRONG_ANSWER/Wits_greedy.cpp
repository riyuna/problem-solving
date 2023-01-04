// Intentionally invalid solution by Abe Wits
// Greedily take smallest subsets with sum 0
// Problem: Bills

#include <iostream>
#include <cstdlib>
#include <set>

using namespace std;

long long balance[20];
int M, N;
set<int> m[21];//map subset to sum

int main () {
	cin >> M >> N;
	for (int i = 0; i < N; i++) {
		int a, b;
		long long p;
		cin >> a >> b >> p;
		balance[a] += p;
		balance[b] -= p;
	}
	for(int mask=0; mask < (1<<(M)); mask++) {
		int sum = 0;
		int set_size = 0;
		for(int i=0; i<M; i++)
			if(mask&(1<<i)) {
				sum+=balance[i];
				set_size++;
			}
		if(sum == 0)
			m[set_size].insert(mask);
	}
	int total_mask = 0;
	int result = 0;
	for(int size = 1; size <= M; size++) {
		for(set<int>::iterator x = m[size].begin(); x!= m[size].end(); ++x) {
			int new_mask = *x;
			if(!(new_mask & total_mask)) {
				total_mask += new_mask;
				result += size-1;
			}
		}
	}
	cout << result << endl;
	return 0;
}

