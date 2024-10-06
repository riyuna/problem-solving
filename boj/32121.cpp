// 君の手を握ってしまったら
// 孤独を知らないこの街には
// もう二度と帰ってくることはできないのでしょう
// 君が手を差し伸べた 光で影が生まれる
// 歌って聞かせて この話の続き
// 連れて行って見たことない星まで
// さユリ - 花の塔


#include<bits/stdc++.h>
#include <queue>
using namespace std;

typedef long long ll;
typedef vector<ll> vll;

const ll w=3;
const ll mod =998244353;



ll pw(ll a, ll b, ll p=mod){
    ll res=1;
    while(b){
        ll r=b%2;
        if(r)res=res*a%p;
        b>>=1;
        a=(a*a)%p;
    }
    return res;
}

void ntt(vll &L, bool inv=false){
    ll sz=L.size();
    ll j=0;
    for(ll i=1;i<sz;i++){
        ll bit=sz>>1;
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
    while(m<=sz){
        ll u=pw(3,mod/m, mod);
        if(inv) u=pw(u,mod-2,mod);
        for(ll i=0;i<sz;i+=m){
            ll w=1;
            for(ll k=i;k<(i+(m/2ll));k++){
                ll tmp=(L[k+(m/2ll)]*w)%mod;
                L[k+(m/2ll)] = (L[k]-tmp+mod)%mod;
                L[k]=(L[k]+tmp)%mod;
                w=(w*u)%mod;
            }
        }
        m*=2;
    }
    if(inv){
        ll inv_n = mod-((mod-1)/sz);
        for(ll i=0;i<sz;i++){
            L[i]=L[i]*inv_n%mod;
        }
    }
}

vll mul(vll _L1, vll _L2){
    vll L1(_L1.begin(), _L1.end()), L2(_L2.begin(), _L2.end());
    ll n=2;
    while(n<L1.size()+L2.size())n<<=1;
    L1.resize(n);
    L2.resize(n);
    ntt(L1);
    ntt(L2);
    for(ll i=0;i<n;i++){
        L1[i]=(L1[i]*L2[i])%mod;
    }
    ntt(L1,true);
    return L1;
}




int main(){
   ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
   int n;
   cin>>n;
   vll res;
   queue<vll> q;
   res.push_back(1);
   q.push(res);
   for(int i=0;i<n-1;i++){
        vll now;
        now.push_back(i*2+2);
        now.push_back(1);
        q.push(now);
   }
   while(q.size()>1){
        vll L1, L2;
        L1=q.front();
        q.pop();
        L2=q.front();
        q.pop();
        vll L = mul(L1, L2);
        q.push(L);
   }
   ll fact=1;
   for(int i=1;i<=n;i++){
        fact*=i;
        fact%=mod;
   }
   cout<<n<<'\n';
   vll L=q.front();
   q.pop();
   for(int i=1;i<=n;i++){
        cout<<i<<' '<<(L[i-1]*fact)%mod<<'\n';
   }
}


