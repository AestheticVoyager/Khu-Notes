import csv

# Specify the file path
csv_file_path = 'housing.csv'
lst = []
# Open the CSV file
with open(csv_file_path, 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Each 'row' is a list representing a row in the CSV file
        for word in row:
            word = float(word)
        lst.append(row)
for i in range(len(lst)):
    for j in range(len(lst[0])):
        lst[i][j]=float(lst[i][j])

y_outs =[]
inputs = []
for i in range(len(lst)):
    y_outs.append([lst[i][3]/ 1000] )
    inputs.append(lst[i][0:3])


