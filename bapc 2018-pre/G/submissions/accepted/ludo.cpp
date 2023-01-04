#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll, ll> ii;
typedef vector<ll> vi;
typedef pair<ll, char> obs;

#define ISG(c) ((c) == 'g')
#define ISY(c) ((c) == 'y')
#define ISR(c) ((c) == 'r')
#define x first
#define y second

ll mod(ll a, ll b) { return (a %= b) < 0 ? (a + b) : a; }

inline ll intersection(ll l1, ll r1, ll l2, ll r2) {
	ll len = min(r1, r2) - max(l1, l2) + 1;
	if(len < 0) return 0;
	return len;
}

ld answerQuery(ll minT, ll maxT, ll G, ll Y, ll R) {
	ll GYR = G + Y + R;
	ll Qt;
	string Qc;
	cin >> Qt >> Qc;
	char ch = Qc[0];

	ll loT, hiT;

	// cerr << "Query at " << (Qt % GYR) << endl;

	if(ISG(ch))
		loT = Qt - G + 1, hiT = Qt;
	else if(ISY(ch))
		loT = Qt - G - Y + 1, hiT = Qt - G;
	else if(ISR(ch))
		loT = Qt - G - Y - R + 1, hiT = Qt - G - Y;
	else
		assert(false);

#ifdef DEBUG
		// cerr << "cycle can start on T ∈ [" << loT << ", " << hiT << "]" << endl;
#endif

	// we must have loT <= T <= hiT.
	loT = mod(loT, GYR);
	hiT = mod(hiT, GYR);
	if(hiT < loT) hiT += GYR;

#ifdef DEBUG
		// cerr << "Cycle can start on T ∈ [" << loT << ", " << hiT << "]" << endl;
		// cerr << "Determining the overlap with [" << minT << ", " << maxT << "]" << endl;
#endif

	ll num = 0;
	for(ll k = -10; k <= 10; k++) { num += intersection(minT, maxT, loT + k * GYR, hiT + k * GYR); }

	ll den = maxT - minT + 1; // [ minT, maxT ]

#ifdef DEBUG
	// cerr << "ANSWER: " << num << " / " << den << endl;
#endif

	return ((ld)1.0) * num / den;
}

int main() {
	ll G, Y, R;
	cin >> G >> Y >> R;

	ll GYR = G + Y + R;
	vector<obs> observations;

	int N;
	cin >> N;
	for(int i = 0; i < N; i++) {
		ll X;
		string S;
		cin >> X >> S;
		X = mod(X, GYR);

		observations.emplace_back(X, S[0]);
		observations.emplace_back(X + GYR, S[0]);
	}

	sort(observations.begin(), observations.end());

	// first green
	int fg = 0;
	if(ISG(observations.back().y)) {
		fg = N;
		while(ISG(observations[fg - 1].y)) fg--;
	} else {
		while(!ISG(observations[fg].y)) fg++;
	}
	assert(fg < N);

	// first yellow
	int fy = fg + 1;
	while(!ISY(observations[fy].y)) fy++;

	// first red
	int fr = fy + 1;
	while(!ISR(observations[fr].y)) fr++;

	assert(fr < fg + N);

	int lg = fy - 1;
	int ly = fr - 1;

	int lr = fr;
	while(lr + 1 < 2 * N && ISR(observations[lr + 1].y)) lr++;

	// colours cannot be mixed up.
	assert(lr == fg + N - 1);

#ifdef DEBUG
	// cerr << "partitioning:" << endl;
	// cerr << "GREEN: idx [" << fg << ", " << lg << "], time [" << observations[fg].x << ", " <<
	// observations[lg].x << "]"; cerr << "YELLOW: idx [" << fy << ", " << ly << "], time [" <<
	// observations[fy].x << ", " << observations[ly].x << "]"; cerr << "RED: idx [" << fr << ", "
	// << lr << "], time [" << observations[fr].x << ", " << observations[lr].x << "]" << endl;
#endif

	// T = time that green light starts.
	// minimal value possible for T:
	ll mint = max(observations[lg].x - G + 1,
	              max(observations[ly].x - G - Y + 1, observations[lr].x - G - Y - R + 1)),
	   maxt = min(observations[fg].x, min(observations[fy].x - G, observations[fr].x - G - Y));

	// non-empty
	assert(mint <= maxt);

#ifdef DEBUG
	// cerr << "times: " << mint << " - " << maxt << endl;
#endif

	// query:
	ld ans = answerQuery(mint, maxt, G, Y, R);

	(cout << fixed).precision(15);
	cout << ans << endl;

	return 0;
}
