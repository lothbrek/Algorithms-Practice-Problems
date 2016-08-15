#Re-creating the Enumerable module to practice and learn Ruby

module Enumerable
	def my_each
		for element in self
			yield(element)
		end
		self
	end

	def my_each_with_index
		index = 0
		self.my_each{|element| yeild(element, index); index +=1}
	end

	def my_select
		result = []
		self.my_each {|element| result << element if yield(element)}
		result
	end

	def my_all?
		self.my_each { |element| return false unless yield(element)}
		true
	end

	def my_any?
		self.my_each{|element| return true if yield(element)}
		false
	end

	def my_none?
		self.my_each{|element| return true unless yield(element)}
		return false
	end

	def my_count
		count = 0
		self.my_each do |element|
			count += if block_given?
				yield(element)?1:0
			else
				1
			end
		end
		count
	end

	#when a block and proc are both provided, the block is run first on the elements,
	#then the proc is run on the result of that block's operation
	def my_map(proc = nil)
		result = []
		if proc && block_given?
			slef.my_each{|element| result << proc.call(yield(element))}
		elsif proc && !block_given?
			self.my_each{|element| result << proc.call(element)}
		elsif proc.nil? && block_given?
			self.my_each{|element|result << yield(element)}
		else
			self
		end
		result
	end

	#injecting into the class
	def my_inject(init = nil)
		init = self[0] if init.nil?
		temp = init
		self.my_each{|element| temp = yield(temp, element)}
		temp
	end

	def multiply_els(a)
		a.my_inject(1) {|x, y| x * y}
	end

end