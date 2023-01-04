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
    vector<int> v(N,0), w;
    for(int i = 0; i < M; i++) {
        int a, b, p;
        cin >> a >> b >> p;
        v[a] -= p;
        v[b] += p;
    }

    // We remove all people with balance 0, as well as all pairs of people who
    // balance each other out, giving a new vector w.
    int set_ct = 0;
    for(int i = 0; i < N; i++) {
        if(v[i] == 0) {
            set_ct++;
            continue;
        }
        for(int j = i + 1; j < N; j++) {
            if(v[i] + v[j] == 0) {
                // If we match a group of 2, we later catch the latter one as
                // a group of one, which updates set_ct.
                v[i] = 0;
                v[j] = 0;
                break; 
            }
        }
    }
    for(int i = 0; i < N; i++) {
        if(v[i]) {
            w.push_back(v[i]);
        }
    }

    // The vector zero_sets contains all bitmasks for groups whose total balance is 0.
    vector<int> zero_sets;
    for(int i = 0; i < (1 << w.size()); i++) {
        int sum = 0;
        for(int j = 0; j < (int)w.size(); j++) {
            if(i & (1 << j)) {
                sum += w[j];
            }
        }
        if(sum == 0)
            zero_sets.push_back(i);
    }

    // For each element of zero_sets, find the largest number of groups with
    // zero balance it can be split into.
    int S = zero_sets.size();
    vector<int> groups(S,0);
    for(int i = 0; i < S; i++) {
        for(int j = 0; j < i; j++) {
            if(!(j & ~i)) { // If j is a submask of i...
                groups[i] = max(groups[i], groups[j] + 1);
            }
        }
    }

    // Finally, correct for the pairs and singles we found at the beginning.
    cout << N - groups[S - 1] - set_ct << endl;
    return 0;
}
