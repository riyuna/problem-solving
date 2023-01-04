#include <bits/stdc++.h>
#define mp make_pair
#define eb emplace_back
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define svec(x) sort(all(x))
#define press(x) x.erase(unique(all(x)), x.end());
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;
typedef pair<int, LL> pil;
typedef pair<LL, int> pli;
typedef pair<LL, LL> pll;
const int INF=1e9;
const LL LLINF=1e18;

int n, m;
LL x[300010], cost;
pair<pii, int> rng[300010];

struct UNION_FIND{
    int par[300010];
    UNION_FIND(){for(int i=1; i<=300000; i++)par[i]=i;}
    int findpar(int num){return num==par[num]?num:par[num]=findpar(par[num]);}
    void mergepar(int a, int b){par[findpar(a)]=findpar(b);}
}uf;

vector<int> ans[300010];
int arr[300010];
bool cmp(pair<pii, int> a, pair<pii, int> b){
    return a.F.S<b.F.S;
}

int main(){
    scanf("%d %d", &n, &m);
    for(int i=1; i<=n; i++)scanf("%lld", &x[i]);
    for(int i=1; i<=n; i++)arr[i]=i;
    for(int i=1; i<=m; i++){
        scanf("%d %d", &rng[i].F.F, &rng[i].F.S);
        arr[rng[i].F.F]=max(arr[rng[i].F.F], rng[i].F.S);
        arr[rng[i].F.S]=max(arr[rng[i].F.S], rng[i].F.F);
        rng[i].S=i;
    }
    sort(rng+1, rng+m+1);
    for(int i=1; i<=n; i++)arr[i]=max(arr[i], arr[i-1]);
    for(int i=1; i<=n; i++)uf.mergepar(i, arr[i]);
    for(int i=1; i<=n; i++)arr[i]=uf.findpar(i);
    int pv=1;
    for(int i=1; i<=n; i++){
        vector<pair<pii, int> > l, r;
        for(; pv<=m; pv++){
            if(rng[pv].F.F>arr[i])break;
            if(rng[pv].F.F<rng[pv].F.S)l.eb(rng[pv]);
            else r.eb(mp(rng[pv].F.S, rng[pv].F.F), rng[pv].S);
        }
        sort(all(l), cmp);
        sort(all(r), cmp);
        LL nw1=x[i], nw2=x[i];
        for(auto j:l){
            cost+=llabs(nw1-j.F.F);
            cost+=llabs(j.F.S-j.F.F);
            nw1=j.F.S;
        }
        for(auto j:r){
            cost+=llabs(nw2-j.F.F);
            cost+=llabs(j.F.S-j.F.F);
            nw2=j.F.S;
        }
        cost+=llabs(nw1-nw2);
        for(auto j:l)ans[i].eb(j.S);
        reverse(all(r));
        for(auto j:r)ans[i].eb(j.S);
    }
    printf("%lld\n", cost);
    for(int i=1; i<=n; i++){
        printf("%d ", ans[i].size());
        for(auto j:ans[i])printf("%d ", j);
        puts("");
    }
}