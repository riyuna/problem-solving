#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll mod = ll(469762049);
vector<ll> mem(1001);

ll pow(ll p, ll n, ll mod){
	if(n<0)return 0;
	if(n==0)return 1;
	if(n==1)return p%mod;
	ll res=1;
	for(;n;n>>=1){
		if(n&1){
			res*=p;
			res%=mod;
		}
		p = (p*p)%mod;
	}
	return res;
}
void NTT(vector<ll> &L, bool inv){
	ll n = L.size();
	ll j=0;
	for(int i=1;i<n;i++){
		ll bit = n>>1;
		while(j>=bit){
			j-=bit;
			bit>>=1;
		}
		j+=bit;
		if(i<j){
			swap(L[i], L[j]);
		}
	}
	ll m=2;
	while(m<=n){
		ll u = pow(3, mod/m, mod);
		if(inv) u = pow(u, mod-2, mod);
		for(int i=0;i<n;i+=m){
			ll w = 1;
			for(int k=i;k<i+m/2;k++){
				ll ind = k+m/2;
				ll tmp = (L[ind]*w)%mod;
				L[ind] = (L[k]-tmp+mod)%mod;
				L[k] += tmp;
				L[k] %= mod;
				w*=u;
				w%=mod;
			}
		}
		m*=2;
		m%=mod;
	}
	if(inv){
		ll inv_n = mod-(mod-1)/n;
		for(int i=0;i<n;i++){
			L[i]=(L[i]*inv_n)%mod;
		}
	}
}

vector<ll> mul(vector<ll> &L1, vector<ll> &L2){
	vector<ll> L11(L1.begin(), L1.end()), L22(L2.begin(), L2.end());
	ll sz1, sz2;
	sz1 = L1.size();
	sz2 = L2.size();
	ll n=1;
	while(n<max(sz1, sz2)) n<<=1;
	n<<=1;
	L11.resize(n);
	L22.resize(n);
	NTT(L11, false);
	NTT(L22, false);
	vector<ll> L;
	for(int i=0;i<n;i++){
		L.push_back((L11[i]*L22[i])%mod);
	}
	NTT(L, true);
	return L;
}

vector<ll> pow2(vector<ll> L, ll n){
	vector<ll> perm;
	perm=mem;
	n-=1;
	while(n){
		if(n&1) perm=mul(perm, L);
		n>>=1;
		L=mul(L, L);
	}
	return perm;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	ll n,k;
	cin>>n>>k;
	vector<ll> L(1001);
	for(int i=0;i<1001;i++){
		L[i]=0;
		mem[i]=0;
	}
	for(int i=0;i<n;i++){
		ll a;
		cin >> a;
		L[a]=1;
		mem[a]=1;
	}
	vector<ll> res;
	res = pow2(L, k);

	for(int i=0;i<res.size();i++){
		if(res[i]) cout<<i<<' ';
	}
	cout<<'\n';
	return 0;
}