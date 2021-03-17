
import fill_list

vector = list();
def Insertion_Sort(vector):
	for i in range(1,len(vector)):
		aux = vector[i]
		j = i
		while j> 0 and vector[j-1] > aux:  
				vector[j] = vector[j-1];
				j -= 1
		vector[j] = aux
	return vector

fill_list.Fill_List(vector)
print("Insertion Sort\n");
print(f"Vector: {vector}\n");
print("After Insertion Sort: ");
print(Insertion_Sort(vector));

