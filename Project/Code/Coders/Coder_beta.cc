#include<iostream>
#include<vector>
#include<fstream>
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
	vector<vector<int>> mat(7842, vector<int> v(1025);
	for (int i = 0; i < 7842; ++i) {
		for int(j = 0; j < 1025; ++j) {
			char n;
			int suma;
			suma = 0;
			for (int k = 0; k < 9; ++k) {
				suma *= 10;
				cin >> n;
				suma += (n -'0');
			}
			mat[i][j] = binary_to_decimal(suma);
		}
	}

}