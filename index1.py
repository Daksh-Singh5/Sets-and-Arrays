# Intersction
set1 = {1,2,3,4,5,6,7}
set2 ={4,5,6,7,8,9}
inter1n2 = set1.intersection(set2)
print("Set1:",set1)
print("Set2:",set2)
print("THe intersection is:",inter1n2)
print("==============================================================")
# Union
set1 = {1,2,3,4,5,6,7}
set2 ={4,5,6,7,8,9}
Union1n2 = set1.union(set2)
print("Set1:",set1)
print("Set2:",set2)
print("THe union is:",Union1n2)
print("==============================================================")
# Difference
set1 = {1,2,3,4,5,6,7}
set2 ={4,5,6,7,8,9}
difference1n2 = set1.difference(set2)
print("Set1:",set1)
print("Set2:",set2)
print("THe difference is:",difference1n2)
print("==============================================================")
# Difference opposite
set1 = {1,2,3,4,5,6,7}
set2 ={4,5,6,7,8,9}
difference1n2 = set2.difference(set1)
print("Set1:",set1)
print("Set2:",set2)
print("THe difference is:",difference1n2)
print("==============================================================")
# symmetric Difference
set1 = {1,2,3,4,5,6,7}
set2 ={4,5,6,7,8,9}
difference1n2 = set2.symmetric_difference(set1)
print("Set1:",set1)
print("Set2:",set2)
print("THe difference is:",difference1n2)
print("==============================================================")