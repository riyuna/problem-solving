#include <bits/stdc++.h>

using namespace std;
const int INF = 1e9;

void sol() {
   int n;
   cin>>n;
   vector<int> v(n);
   for (auto &i:v) cin>>i;
   int mx=0;
   for (int i=0; i<n; i++) {
      if (i&&v[i-1]==v[i]) continue;
      int cnt=1;
      for (int j=i; j<n; cnt++) {
         int b=lower_bound(v.begin()+j+1, v.end(), v[j]*2-v[i])-v.begin();
         if (b>=n) break;
         j=b;
      }
      mx=max(mx, cnt);
   }
   cout<<n-mx<<'\n';
}

int main() {
   cin.tie(0)->sync_with_stdio(0);

   int t;
   cin>>t;
   while (t--) sol();

   return 0;
}