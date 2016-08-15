#this is another algorithm that is very common.
#this algorithm picks the best index combinations for when you would have
#the maximum profit for your stocks(or profits for that day)

def stock_picker(a)
	max = -1
	ret = []
	a.length.times do |x|
		x.upto(a.length - 1) do |y|
			if a[y] - a[x] > max and y > x
				ret = [x, y]
				max = a[y] - a[x]
			end
		end
	end

 	print ret
end

#result is [1,4] 
stock_picker([17,3,6,9,15,8,6,1,10])