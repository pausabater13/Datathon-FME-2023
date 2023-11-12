#include <iostream>
using namespace std;


void binary_to_decimal(int& n) {
	int suma, prod;
	prod = 1;
	suma = 0;
	for (int i = 0; i < 9; ++i) {
		suma += (n%10)*prod;
		prod *= 2;
		n /= 10;
	}
	n = suma;
}

int main () {
	char n;
	int suma;
	suma = 0;
	for (int i = 0; i < 9; ++i) {
		suma *= 10;
		cin >> n;
		suma += (n -'0');
	}
	binary_to_decimal(suma);
	cout << suma << endl;
}