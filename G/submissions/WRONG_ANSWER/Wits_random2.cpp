// Intentionally invalid solution by Abe Wits
// Randomly take subsets with sum 0
// (Small edit by Mees to avoid RTEs.)
// Problem: Bills

#include <iostream>
#include <cstdlib>
#include <vector>

using namespace std;

long long balance[20];
int M, N;
vector<int> m[21];//map subset to sum

int main () {
	cin >> M >> N;
	for (int i = 0; i < N; i++) {
		int a, b;
		long long p;
		cin >> a >> b >> p;
		balance[a] += p;
		balance[b] -= p;
	}
	for (int i = 0; i < M; ++i) {
		if (balance[i] == 0) {
			if (i + 1 < M) {
				swap(balance[i], balance[M - 1]);
				--i;
			}
			--M;
		}
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
			m[set_size].push_back(mask);
	}
	srand(42);
	int best_result = max(M - 1, 0);
	for(int i=0; i<10000; i++) {
		int total_mask = 0;
		int result = 0;
		int size_left = M;
		for(int j=0; j<1000 && size_left > 0 && result < best_result; j++) {
			int size;
			if(size_left == 1) {
				size = 1;
			} else {
				do {
					size = rand()%(size_left)+1;
				} while(m[size].size() == 0);
			}
			int index = rand()%(m[size].size());
			int new_mask = m[size][index];
			if(!(new_mask & total_mask)) {
				total_mask += new_mask;
				result += max(size-1,0);
				size_left -= size;
			}
		}
		result += max(size_left-1,0);
		if(result < best_result)
			best_result = result;
	}
	cout << best_result << endl;
	return 0;
}

