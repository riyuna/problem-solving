// Intentionally invalid solution by Abe Wits
// Problem: Bills

#include <iostream>
#include <cstdlib>
#include <bitset>

using namespace std;

long long balance[20];
int M, N;


int main () {
	cin >> M >> N;
	for (int i = 0; i < N; i++) {
		int a, b;
		long long p;
		cin >> a >> b >> p;
		balance[a] += p;
		balance[b] -= p;
	}
	srand(42);//Program should be deterministic

	int result = 0;

	for(int iteration_count=0; M>0; iteration_count++) {
		int max_target_size = 1+iteration_count / 50000;
	
		int subset = 0;
		int sum = 0;
		int subset_size = 0;
		do {
			int rand_element;//Add random element
			do {
				rand_element = rand()%M;
			} while(subset&(1<<rand_element));
			subset+=(1<<rand_element);
			sum+=balance[rand_element];
			subset_size++;
			if(sum == 0) 
				break;
			for(int i=0; i<M; i++) {//If possible, complete set
				if(subset&(1<<i))//only consider i outside set
					continue;
				if(sum + balance[i] == 0) {
					subset+=(1<<i);
					sum+=balance[i];
					subset_size++;
				}
			}
		} while(sum != 0 && subset_size <= max_target_size);

		if(subset_size > max_target_size) {
			continue;//throw out subset: too big thus likely not optimal
		} else {
			result += subset_size-1;
			int j=0;
			for(int i=0; i<M; i++) {
				if(!((1<<i)&subset)) {//Remove subset from problem
					balance[j]=balance[i];
					j++;
				}
			}
			M-=subset_size;
		}
	}
	cout << result+((M-1)>0?M-1:0) << endl;
	return 0;
}
