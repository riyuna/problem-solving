#include <bits/stdc++.h>
using namespace std;

using ll = long long;
using ii = pair<ll, ll>;
using vii = vector<ii>;

ii get_LU(ll To, string o, ll Tg, ll Ty, ll Tr, ll T) {
	To %= T;

	ll L = To, U = To;
	if (o == "green" ) L -= Tg,           U -= 0;
	if (o == "yellow") L -= Tg + Ty,      U -= Tg;
	if (o == "red"   ) L -= Tg + Ty + Tr, U -= Tg + Ty;
	L = (L % T + T) % T, U = (U % T + T) % T;

	return {L, U};
}

	
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	ll Tg, Ty, Tr, T;
	cin >> Tg >> Ty >> Tr;
	T = Tg + Ty + Tr;

	int n;
	cin >> n;
	vii exc;
	while (n--) {
		ll To, L, U;
		string o;
		cin >> To >> o;
		tie(L, U) = get_LU(To, o, Tg, Ty, Tr, T);

		if (L <= U) {
			if (L > 0) exc.push_back(ii{0, L});
			if (U < T) exc.push_back(ii{U, T});
		} else exc.push_back(ii{U, L});
	}
	exc.push_back(ii{T, T});

	ll Tq, Lq, Uq;
	string q;
	cin >> Tq >> q;
	tie(Lq, Uq) = get_LU(Tq, q, Tg, Ty, Tr, T);

	sort(exc.begin(), exc.end());
	ll frac = 0LL, full = 0LL, last = 0LL;
	for (ii pr : exc) {
		if (pr.first <= last)
			last = max(last, pr.second);
		else {
			full += pr.first - last;
			if (Lq <= Uq)
				frac += max(0LL, min(pr.first, Uq) - max(last, Lq));
			else
				frac += max(0LL, min(pr.first, Uq) - last),
				frac += max(0LL, pr.first - max(last, Lq));
			last = pr.second;
		}
	}

	printf("%.10lf\n", double(frac) / double(full));

	return 0;
}
