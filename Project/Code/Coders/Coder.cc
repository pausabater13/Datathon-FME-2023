#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

// Convert binary to decimal directly without modifying the input parameter
int binary_to_decimal(const string& binary) {
    int decimal = 0;
    int prod = 1;

    for (int i = 8; i >= 0; --i) {
        decimal += (binary[i] - '0') * prod;
        prod *= 2;
    }

    return decimal;
}

int main() {
    const int rows = 7842;
    const int cols = 1025;

    vector<vector<int>> mat(rows, vector<int>(cols));

    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            string binary;
            cin >> binary;

            mat[i][j] = binary_to_decimal(binary);
        }
    }

    // Save the matrix to a CSV file
    ofstream outputFile("output_matrix.csv");
    if (outputFile.is_open()) {
        for (const auto& row : mat) {
            for (int value : row) {
                outputFile << value << ",";
            }
            outputFile.seekp(-1, ios_base::cur); // Remove the trailing comma
            outputFile << "\n";
        }
        outputFile.close();
        cout << "Matrix saved to output_matrix.csv\n";
    } else {
        cerr << "Unable to open the output file.\n";
    }

    return 0;
}