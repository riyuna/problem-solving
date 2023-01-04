#include<bits/stdc++.h>
using namespace std;
int main()
{
	int n, p, q, r, ans = 0;
	string s;
	cin >> n >> p >> q >> r >> s;
	vector<int> ch(n);

	for (int i = 0; i < n; i++) { //이미 존재하는 SKH 카운트
		if (i >= 2 && s[i - 2] == 'S' && s[i - 1] == 'K' && s[i] == 'H') {
			ch[i - 2] = ch[i - 1] = ch[i] = 1;
			ans++;
		}
	}

	for (int i = 1; i < n; i++) { //하나만 사용해도 되는 것들
		if (ch[i - 1] || ch[i])continue;
		if (s[i - 1] == 'S' && s[i] == 'K' && r > 0) {
			ch[i - 1] = ch[i] = 1;
			r--;
			ans++;
		}
		else if (s[i - 1] == 'S' && s[i] == 'H' && q > 0) {
			ch[i - 1] = ch[i] = 1;
			q--;
			ans++;
		}
		else if (s[i - 1] == 'K' && s[i] == 'H' && p > 0) {
			ch[i - 1] = ch[i] = 1;
			p--;
			ans++;
		}
	}

	int cnt[3] = { 0 };//S, K, H
	for (int i = 0; i < n; i++) {
		if (ch[i] == 0) {
			if (s[i] == 'S')cnt[0]++;
			else if (s[i] == 'K')cnt[1]++;
			else cnt[2]++;
		}
	}

	while (1) { //2개 써야 하는 것들
		int x = min({ cnt[0],q,r }), y = min({ cnt[1],p,r }), z = min({ cnt[2],p,q });
		if (max({ x,y,z }) == 0) break;
		else if (max({ x,y,z }) == x) {
			cnt[0] -= x;
			q -= x;
			r -= x;
			ans += x;
		}
		else if (max({ x,y,z }) == y) {
			cnt[1] -= y;
			p -= y;
			r -= y;
			ans += y;
		}
		else {
			cnt[2] -= z;
			p -= z;
			q -= z;
			ans += z;
		}
	}

	ans += min({ p,q,r });// 3개 다 써야 하는 것들 
	cout << ans;
	return 0;
}