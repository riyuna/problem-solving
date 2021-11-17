#include <iostream>
#include <bits/stdc++.h>
#define fastio cin.tie(0)->sync_with_stdio(0)
#define ull unsigned long long
using namespace std;

string s1, s2, ans;

int lcs(string s1, string s2){
    int n=s1.size();
    int m=s2.size();
    int size = (m>>6)+1;

    vector<ull>L[256];
    for(int i=0;i<256;i++) L[i].resize(size);
    for(int i=0;i<m;i++) L[s2[i]][i>>6] |= 1llu<<(i&63);
    vector<ull> row(size);
    for(int i=0;i<m;i++){
        if(s1[0]==s2[i]){
            row[i>>6] |= 1llu<<(i&63);
            break;
        }
    }

    for(int i=1;i<n;i++){
        ull a=1;
        ull b=0;
        for(int j=0;j<size;j++){
            ull x=L[s1[i]][j] | row[j];
            ull tmp=(row[j]<<1)|a;
            a=row[j]>>63;

            auto fill = [](ull &xx, ull y){
                ull tmp2=xx;
                return (xx=tmp2-y)>tmp2;
            };
            ull tmp3=x;
            b=fill(tmp3, b);
            b+=fill(tmp3, tmp);
            row[j]=x&(x^tmp3);
        }
        row[m>>6] &= (1llu<<(m&63))-1;
    }
    int res=0;
    for(int i=0;i<m;i++){
        if(((row[i>>6] >> (i&63))&1) == 1) res++;
    }
    return res;
}

int main(){
    fastio;
    cin >> s1 >> s2;
    int ans=0;
    for(int i=-0;i<int(s2.size());i++){
        ans=max(ans, lcs(s1,s2));
        rotate(s2.begin(), s2.begin()+1, s2.end());
    }
    reverse(s2.begin(), s2.end());
    for(int i=-0;i<int(s2.size());i++){
        ans=max(ans, lcs(s1,s2));
        rotate(s2.begin(), s2.begin()+1, s2.end());
    }
    cout<< ans << endl;
    return 0;
}