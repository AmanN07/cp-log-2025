
#include<iostream>
using namespace std;

const int MOD = 998244353;

int main() {
	// your code goes here
	int T;
	cin>>T;

	while (T--)
	{
		int N;
		cin>>N;
		vector<int> A(N);

		for(int i=0; i< N; ++i){
			cin>>A[i];
		}
	sort(A.begin(), A.end());

	long long result = 1;
	bool possible = true;

	for (int i=0; i<N; ++i){
		int options = A[i] - i;
		if(options <= 0){
			possible = false;
			break;
		}
		result = (result*options) % MOD;
	}
	if (!possible) cout<< 0<< "\n";
	else cout<<result<<"\n";
	}
	return 0;
}
