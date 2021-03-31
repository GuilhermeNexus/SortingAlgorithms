import Fill_List_Python

list = list()

Fill_List_Python.Fill_List(list)

print(list)

def Quick_Sort(list):
	length = len(list)
	if length <= 1:
		return list
	else:
		pivot = list.pop()
	lesser_list = []
	greater_list = []

	for i in list:
		if i > pivot:
				greater_list.append(i)
		else:
				lesser_list.append(i)
	return Quick_Sort(lesser_list) + [pivot] + Quick_Sort(greater_list)

print(Quick_Sort(list))
