#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
ll mod = ll(998244353);

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
	ll sz1, sz2;
	sz1 = L1.size();
	sz2 = L2.size();
	ll n=1;
	while(n<max(sz1, sz2)) n<<=1;
	n<<=1;
	L1.resize(n);
	L2.resize(n);
	NTT(L1, false);
	NTT(L2, false);
	vector<ll> L;
	for(int i=0;i<n;i++){
		L.push_back((L1[i]*L2[i])%mod);
	}
	NTT(L, true);
	return L;
}

int main(){
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n,m;
	cin>>n>>m;
	vector<ll> L1, L2;
	ll p;
	for(int i=0;i<n;i++){
		cin>>p;
		L1.push_back(p);
	}
	for(int i=0;i<m;i++){
		cin>>p;
		L2.push_back(p);
	}
	vector<ll> res = mul(L1, L2);
	n=res.size();
	for(int i=0;i<n;i++){
		cout<<res[i]<<' ';
	}
	return 0;
}