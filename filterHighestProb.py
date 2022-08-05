import csv
from collections import defaultdict

columns = defaultdict(list)

input_path = "result1.csv"
output_path = "result1reduced.csv"

with open(input_path) as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            columns[k].append(v)

maxProb = max(columns['probability'])
print(maxProb)

reduced_inputs = defaultdict(columns.default_factory, filter(lambda i: i[1] == maxProb, columns.items()))

print(reduced_inputs)
