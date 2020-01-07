import ast
import csv
with open('classicKNN_file2.csv') as csv_file:
    csv_reader=csv.reader(csv_file)
    for row in csv_reader:
        print(row[6:28])
        for i in range (len(row)):
            print(row[i])
        print(ast.literal_eval(row[7])+5)
        break