require 'C:\Users\hroch\Documents\GitHub\SortingAlgorithms\Fill_List_Ruby'
list = Array.new
Fill_List(list)

list.each do |i|
print String(i) + " "
end
puts ""


for i in 0..list.size - 1
	minimum = i
	for j in i+1..list.size - 1
		if list[minimum] < list[j]
			minimum = j
		end
	end
	if minimum != i
		list[minimum], list[i] = list[i], list[minimum]
	end
end

puts ""
list.reverse.each do |i|
print String(i) + " "
end
