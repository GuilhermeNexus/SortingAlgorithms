require_relative "Fill_List_Ruby"

list = Array.new

Fill_List(list)
print(list)
def Quick_Sort(list)

return list if list.size <= 1

pivot = list.pop
lower_list = Array.new
higher_list = Array.new
list.each do |i|
	if i > pivot
		higher_list << (i)
	else
		lower_list << (i)
	end
end
return Quick_Sort(lower_list) + [pivot] + Quick_Sort(higher_list)
end
puts ""
print(Quick_Sort(list))