#include<bits/stdc++.h>

using namespace std;

#define nl '\n'
#define fi first
#define se second

typedef long long ll;

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
	int tests = 1;
	cin>>tests;
	cout<<nl;
	for(int i = 1; i <= tests; i++){
		int a, b;
		cin>>a>>b;
		cout<<a + b;
		if(i < tests) cout<<nl;
	}
}