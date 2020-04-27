from os import listdir
import csv

# for i in listdir("dataFiles"):
#     file = open("dataFiles/"+i, "r")
#     data = csv.reader(file)
#     for j in data:
#         try:
#             j.remove('')
#         except:
#             pass
#         for k in range(len(j)):
#             if j[k].isdigit():
#                 j[k] = int(j[k])
#         print(tuple(j), ",")
#     print("\n\n\n\n")


file = open("dataFiles/Comment.csv", "r")
data = csv.reader(file)
for j in data:
    j = j[:5]
    for k in range(len(j)):
        if j[k].isdigit():
            j[k] = int(j[k])
    print(tuple(j), ",")
print("\n\n\n\n")