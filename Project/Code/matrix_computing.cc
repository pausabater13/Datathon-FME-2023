#include <iostream>
#include <fstream>
#include <vector>
#include <csv.h>

int main() {
    std::string filename = "../../datathon-2023-fashion-compatibility-main/datathon/dataset/outfit_data.csv";// Specify the path to your CSV file
    std::ifstream file(filename);// Open the CSV file
    
    // Check if the file is open
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << filename << std::endl;
        return 1; // Return an error code
    }
    
    csv::CSVReader csv_reader(file);// Create a CSV reader    
    std::vector<std::vector<int>> data;// Create a vector to store the data

    // Iterate over the rows in the CSV file
    for (csv::CSVRow& row : csv_reader) {
        std::vector<int> rowData;// Create a vector to store the current row
        for (const csv::CSVField& field : row) // Iterate over the values in the current row
            // Convert the field to an integer and add it to the row
            rowData.push_back(field.get<int>());
        
        data.push_back(rowData);// Add the row to the data vector
    }

    // Close the file (optional, as it will be closed when 'file' goes out of scope)

    // Print the data
    for (const auto& row : data) {
        for (int value : row)
            std::cout << value << " ";
        std::cout << std::endl;
    }

    return 0; // Return success
}
