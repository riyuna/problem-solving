#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <stack>

using namespace std;

#define endl '\n'
#define mp make_pair

typedef pair<int,int> pii;
typedef vector<int> vi;

int LSOne(int i) {
	return i & (-i);
}

class FenwickTree {
	private: vi ft;
	// recall that vi is: typedef vector<int> vi;
	public: FenwickTree(int n) { ft.assign(n + 1, 0); }
	// init n + 1 zeroes
	int rsq(int b) {
	// returns RSQ(1, b)
	int sum = 0; for (; b; b -= LSOne(b)) sum = max(sum,ft[b]);
	return sum; }
	// note: LSOne(S) (S & (-S))
	int rsq(int a, int b) {
	// returns RSQ(a, b)
	return rsq(b) - (a == 1 ? 0 : rsq(a - 1)); }
	// adjusts value of the k-th element by v (v can be +ve/inc or -ve/dec)
	void adjust(int k, int v) {
	// note: n = ft.size() - 1
	for (; k < (int)ft.size(); k += LSOne(k)) { /*clog << k << endl;*/ ft[k] = max(ft[k],v);} }
};

int flipp(int a, int y){
	if(a < y) 	return y + (y-a);
	else 		return y - (a-y);
}

bool isCandidate(int ax, int ay, int bx, int by, int x, int y){
	return (ax <= x && x <= bx && ay <= y && y <= by);
}

int main(){
	//Readin input
	int N;
	cin >> N;
	int ax, ay, bx, by;
	cin >> ax >> ay >> bx >> by;
	ax++; ay++; bx++; by++;

	//Make sure we go from bottom left to top right
	if(ax > bx){
		swap(ax,bx);
		swap(ay,by);
	}
	bool flip = (ay > by);
	if(flip) ay = flipp(ay,by);
	int mini = min(ay,by);

	//Readin input - translate coordinates to the box
	vector<pii> cs;
	for(int i = 0; i < N; i++){
		int x, y;
		cin >> x >> y;
		x++; y++;
		if(flip) y = flipp(y,by);
		if(isCandidate(ax,ay,bx,by,x,y)){
			cs.push_back({x,y});
			mini = min(mini,y);
		}
	}

	//Make all coordinates positive > 0
	if(mini < 1){
		mini -= 1;
		ax -= mini; 
		ay -= mini; 
		bx -= mini; 
		by -= mini; 
		for(int i = 0; i < cs.size(); i++){
			cs[i].first -= mini;
			cs[i].second -= mini; 	
		}
	}

	//COmpress y coordinates
	set<int> yvals;
	map<int,int> ylink;
	for(int i = 0; i < cs.size(); i++){
		yvals.insert(cs[i].second);
	}
	int cnt = 1;
	for(int i : yvals){
		if(!ylink[i]) { ylink[i] = cnt; cnt++; }
	}
	if(!ylink[by]){ylink[by] = cnt; cnt++; }

	//Solve the problem
	sort(cs.begin(),cs.end());
	FenwickTree cur(cnt);
	for(int i = 0; i < cs.size(); i++){
		pii p = cs[i];
		int best = cur.rsq(ylink[p.second]);
		cur.adjust(ylink[p.second],best + 1);
	}
	cout << cur.rsq(ylink[by]) << endl;

	return 0;
}