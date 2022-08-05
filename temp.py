# import csv
from collections import defaultdict

# columns = defaultdict(list)

# with open("result1.csv") as f:
#     reader = csv.DictReader(f)  # read rows into a dictionary format
#         # read a row as {column1: value1, column2: value2,...}
#     for row in reader:
#         for (k, v) in row.items():  # go over each column name and value
#                 # append the value into the appropriate list
#             columns[k].append(v)
#                                     # based on column name k

#     # input_file = open("input.txt", "r")
#     # file_content = input_file.read()

#     # inputs = file_content.split("\n")
# inputs = columns['sbox2output']
# print(inputs)

# def split2(a):
#     arr = [a >> 32]
#     arr += [a & 0xffffffff]
#     return arr

import csv

columns = defaultdict(list)

with open("result1.csv") as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        for (k,v) in row.items(): # go over each column name and value 
            columns[k].append(v)

print(min(columns['probability'])) 
print(max(columns['probability'])) 