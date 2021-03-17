import Fill_List_Python
list = list()

Fill_List_Python.Fill_List(list)

print(list)

for i in range(len(list)-1):
	minimum = i
	for j in range(i+1,len(list)):

		if list[j] < list[minimum]:
			minimum = j
	if minimum != i:
		list[minimum], list[i] = list[i], list[minimum]


print("\n")
print(list)

