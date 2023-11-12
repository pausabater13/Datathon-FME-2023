#include <iostream>
using namespace std;


void decimal_to_binary (int n,int b) {
	if (b == 1) cout << n%2;
	else {
		decimal_to_binary(n/2,b-1);
		cout << n%2;
	}
}

int main () {
	int n;
	cin >> n;
	decimal_to_binary(n,9);
	cout << endl;
}