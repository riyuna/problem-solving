#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef pair<int, int> llp;

int dp[510][510];
int n, ct;
ll x, y, x_1, y_1;
llp v[510], tempv[510];

ll dist(llp p1, llp p2){
	return (p1.first-p2.first)*(p1.first-p2.first) + (p1.second-p2.second)*(p1.second-p2.second);
}

int ccw(llp p1, llp p2, llp p3){
	ll res = (ll) ((ll) p1.first*p2.second + (ll) p2.first*p3.second + (ll) p3.first*p1.second) - (ll) ((ll) p1.second*p2.first + (ll) p2.second*p3.first + (ll) p3.second*p1.first);
	if(res==0)return 0;
	return (res>0)?1:-1;
}

bool cp1(llp p1, llp p2){
	// x축 기준. 같으면 y축 기준
	if(p1.first==p2.first){
		return p1.second-p2.second;

	}
	return (p1.first<p2.first);
}

bool cmp(llp p1, llp p2){
	/* (0,0)을 기준으로 정렬*/
	llp p = make_pair((ll) 0, (ll) 0);
	ll dir = ccw(p, p1, p2);
	if(dir!=0)return (dir>0);
	return (dist(p, p1)<dist(p, p2));
}

bool inside(llp p1, llp p2, llp p3, llp p){
	return((ccw(p1, p2, p)==ccw(p2, p3, p)) and (ccw(p2, p3, p)==ccw(p3, p1, p)));
}

int main(){
	cin.tie(NULL);
    ios_base::sync_with_stdio(false);
	ct=0;
	cin >> n;

	for(int i=0;i<n;i++){
		cin >> x >> y;
		tempv[i] = make_pair(x, y);
	}
	sort(tempv, tempv+n, cp1);

	x_1 = tempv[0].first;
	y_1 = tempv[0].second;

	for(int i=0;i<n;i++){
		v[i] = make_pair(tempv[i].first-x_1, tempv[i].second-y_1);
	}

	sort(v+1,v+n, cmp);

	// for(int i=0;i<n;i++){
	// 	cout << v[i].first << ' ' << v[i].second << endl;
	// }

	// cout << "#################" << endl;

	for(int i=1;i<n;i++){
		for(int j=i+1;j<n;j++){
			int count = 0;
			for(int k=1;k<n;k++){
				if((k==i) or (k==j))continue;
				if(inside(v[0], v[i], v[j], v[k]))count++;
			}
			// cout << i << ' ' << j << ' ' << count << endl; 
			dp[i][j]=count;
			if(count>0)ct++;
		}
	}
	// cout << "#################" << endl;

	for(int i=1;i<n;i++){
		for(int j=i;j<n;j++){
			for(int k=j;k<n;k++){
				int res = 0;
				if(inside(v[0], v[i], v[k], v[j])){
					res = dp[i][k] - dp[i][j] - dp[j][k] -1;
				}
				else{
					res = dp[i][j] + dp[j][k] - dp[i][k];
				}
				// cout << i << ' ' <<  j << ' ' << k << ' ' << res << endl;
				if(res>0)ct++;
			}
		}
	}
	cout << ct << endl;
	return 0;
}