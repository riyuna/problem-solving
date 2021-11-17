#include <iostream>
#include <queue>

using namespace std;

int main()
{
   long long n;
   cin >> n;
   long long L[10030];
   for(long long i=0;i<n;i++)cin>>L[i];
   long long cnt;
   cnt=0;
   while(1){
       long long mi=0;
       long long pt=-1;
       for(long long i=0;i<n;i++){
           if(L[i]<mi){
               mi=L[i];
               pt=i;
           }
       }
       if(pt==-1)break;
       cnt++;
       L[(pt+n-1)%n]+=mi;
       L[(pt+1)%n]+=mi;
       L[pt]=-1*L[pt];
   }
   cout << cnt << endl;
   return 0;
}