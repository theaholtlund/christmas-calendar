# Kode24's Christmas Calendar

# Import required libraries
import pandas as pd

# Find the delimiter used for the file (for fun)
with open('animals.dat', 'r') as file:
    first_line = file.readline()
    possible_delimiters = [',', '\t', ';', ' ']

    for delimiter in possible_delimiters:
        if delimiter in first_line:
            if delimiter == ' ':
                print("The delimiter is a space.")
            elif delimiter == '\t':
                print("The delimiter is a tab.")
            else:
                print(f"The delimiter is: {delimiter}")
            break

# Moving on, concluding that the file is tab separated
data = pd.read_csv('animals.dat', delimiter='\t')

# Identify the greatest value for each column
max_values = data.max()

# Identify what column holds the greatest value
max_column = max_values.idxmax()

# Find the single greatest number in the dataset
greatest_number = data.max().max()

print(f"The greatest number for each column is: {max_values}")
print(f"The column with the highest maximum value is: {max_column}")
print(f"The single greatest number in the dataset is: {greatest_number}")
