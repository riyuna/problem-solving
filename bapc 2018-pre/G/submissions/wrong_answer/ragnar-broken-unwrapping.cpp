#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
using namespace std;
int main(){
	array<int, 3> ts;
	for(auto &x : ts) cin >> x;
	int T = ts[0] + ts[1] + ts[2];
	int n;
	cin >> n;
	array<vector<int>, 3> o;
	while(n--){
		int t;
		string c;
		cin >> t >> c;
		t %= T;
		if(c=="green") o[0].push_back(t);
		else if(c=="yellow") o[1].push_back(t);
		else if(c=="red") o[2].push_back(t);
		//else assert(false);
	}
	for(auto &x : o) sort(x.begin(), x.end());
	// Make sure all intervals are non-wrapping, and the times are increasing.
	int last = -1;
	for(int i = 0; i < 3; ++i){
		int j = (i+1)%3;
		//assert(!o[j].empty());
		int cut = o[j][0];
		for(auto &x : o[i])
			while(x < cut || x < last) last = x += T; // Executes at most twice.
	}
	//assert(o[2].back() - o[0].front() < T);
	// Find minimal valid offset.
	int t_min = max(o[0].back() - ts[0], max(o[1].back() - ts[0] - ts[1], o[2].back() - T));
	int t_max = min(o[0].front(), min(o[1].front() - ts[0], o[2].front() - ts[0] - ts[1]));
	//assert(t_min < t_max);
	// Answer query.
	int tq;
	string sq;
	cin >> tq >> sq;
	tq %= T;
	int i_min, i_max;
	if(sq == "green"){
		i_min = tq - ts[0];
		i_max = tq;
	} else if(sq == "yellow"){
		i_min = tq - ts[0] - ts[1];
		i_max = tq - ts[0];
	} else if(sq == "red"){
		i_min = tq - ts[0] - ts[1] - ts[2];
		i_max = tq - ts[0] - ts[1];
	} //else
		//assert(false);
	while(i_max <= t_min) i_min += T, i_max += T;
	int len = max(min(t_max, i_max) - max(t_min, i_min),0);
	cout << setprecision(15) << double(len)/(t_max - t_min) << endl;
}
