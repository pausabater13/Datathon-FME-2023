#include <iostream>
#include <fstream>
#include <vector>
#include <bitset>
#include <sstream>

// Function to convert an integer to binary string
std::string intToBinaryString(int value) {
    return std::bitset<9>(value).to_string();
}

// Function to convert a matrix of integers to a vector of binary strings
std::vector<std::string> matrixToBinaryStrings(const std::vector<std::vector<int>>& matrix) {
    std::vector<std::string> result;

    for (const auto& row : matrix) {
        std::ostringstream rowResult;

        for (int value : row) {
            rowResult << intToBinaryString(value) << " ";
        }

        result.push_back(rowResult.str());
    }

    return result;
}

int main() {
    const int rows = 7842;
    const int cols = 1025;

    // Create a matrix of integers from 0 to 511
    std::vector<std::vector<int>> myMatrix(rows, std::vector<int>(cols));
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            myMatrix[i][j] = (i * cols + j) % 512;
        }
    }

    // Transform the matrix into a vector of binary strings
    std::vector<std::string> binaryStrings = matrixToBinaryStrings(myMatrix);

    // Write the binary strings to a CSV file
    std::ofstream outputFile("output_matrix.csv");
    if (outputFile.is_open()) {
        for (const std::string& binaryString : binaryStrings) {
            outputFile << binaryString << "\n";
        }
        outputFile.close();
        std::cout << "Binary strings saved to output_matrix.csv\n";
    } else {
        std::cerr << "Unable to open the output file.\n";
    }

    return 0;
}