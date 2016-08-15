#Bubble Sort implemented in Ruby
#shows clearly the power and simplicity of Ruby

def bubble_sort(a)
	(1...a.length).each do |iter|
		(0...a.length-iter).each do|index|
			if a[index] > a[index+1]
				a[index], a[index+1] = a[index+1], a[index]
			end
		end
	end
	a
end

puts bubble_sort([4,3,78,2,0,2])

#sorts an array but accepts a block
def bubble_sort_by(a)
	return unless block_given?
	(1...a.length).each do |iter|
		(0...a.length-iter).each do |index|
			if yield(a[index],a[index+1])>0
				a[index], a[index+1] = a[index+1],a[index]
			end
		end
	end
	a
end