#basic caesar_cipher implementation in ruby
def caesar_cipher(s, n)
	alphabet = [*'a'..'z']
	s.chars.map {|x| alphabet.include?(x.downcase) ? (x.ord + n).chr : x}.join
end

puts caesar_cipher("This Is a Test", 1)
puts caesar_cipher("Breaking news! There is an outbreak of odd lettering", 3)
