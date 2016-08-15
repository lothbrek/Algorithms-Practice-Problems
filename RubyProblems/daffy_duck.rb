#this was a fun program to practice ruby string manipulation
#Daffytizing your words! Thuffering Thuckatash!

print "Please list your daffytizing statement"
user_input = gets.chomp
user_input.downcase!

if user_input.include? "s"
    user_input.gsub!(/s/, "th")
elsif user_input.empty?
    print "I repeat, PUH_LEASE enter your statement to be daffytized: "
    user_input = gets.chomp
    user_input.downcase!
else
    user_input = user_input
end

puts "Your string is now: #{user_input}!"