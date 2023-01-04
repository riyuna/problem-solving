// Solution to: Bills
// By: Mees
//
// Quadratic algorithm (over the set of bitmasks), which is too slow. Could be
// seen as a slower version of Raymond-accepted which does not cleverly look
// for predecessors.
//
// Expected result: TLE

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <climits>

using namespace std;

int main() {
    int N, M; cin >> N >> M;
    // v contains the initial balances for each person.
    vector<int> v(N,0);
    for(int i = 0; i < M; i++) {
        int a, b, p;
        cin >> a >> b >> p;
        v[a] -= p;
        v[b] += p;
    }

    int S = 1 << N;
    vector<int> groups(S, 0);

    for(int i = 0; i < S; i++) {

        int sum = 0;
        for(int k = 0; k < N; k++) {
            if(i & (1 << k)) {
                sum += v[k];
            }
        }
        int zero_set;
        if(sum == 0) {
            zero_set = 1;
        }
        else {
            zero_set = 0;
        }

        for(int j = 0; j < i; j++) {
            if(!(j & ~i)) { // If j is a submask of i...
                groups[i] = max(groups[i], groups[j] + zero_set);
            }
        }
    }

    cout << N - groups[S - 1] << endl;
    return 0;
}
