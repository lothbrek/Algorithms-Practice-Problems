#showing how simply ruby can create custom substring method and a few examples
def substrings(s, dict)
	s.downcase!
	count = {}

	dict.each do |word|
		counts = s.scan(word).length
		count[word] = counts unless < 1
	end
	count
end

dictionary = ["below", "down", "go", "going", "horn", "how", "howdy", "it", "i", "low", "own", "part", "partner", "sit"]
substrings("below", dictionary)
substrings("Howdy partner, sit down! How's it going?", dictionary)

puts "Please enter the sentence you wish to record: "
text = gets.chomp
puts "What is the redacted word/phrase? "
redact = gets.chomp

words = text.split(" ")

words.each do |letter|
    if letter == redact
        print "REDACTED "
    else
        print letter + " "
    end
end