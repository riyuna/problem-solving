#include <iostream>
using namespace std;

int main(){
    int n;
    cin >> n;
    int L[n];
    int m=0;
    int sum=0;
    for(int i=0;i<n;i++){
        cin >> L[i];
        if(L[i]>m)m=L[i];
        sum+=L[i];
        }
    int dp[n][n+1][m*2+1];
    for(int j=0;j<=n;j++){
        for(int i=0;i<n;i++){
            for(int k=0;k<=2*m;k++){
                if(j==0)dp[i][j][k]=(k-m);
                else if(k<=m){
                    dp[i][j][k] = max(dp[(i+1)%n][j-1][k+L[i]], dp[i][j-1][k+L[(i+j-1)%n]]);
                }
                else{
                    dp[i][j][k] = min(dp[(i+1)%n][j-1][k-L[i]], dp[i][j-1][k-L[(i+j-1)%n]]);
                }
            }
        }
    }
    int res = 0;
    for(int i=0;i<n;i++){
        int j = dp[i][n][m];
        if(res<j)res=j;
    }
    cout<<(sum+res)/2;
}