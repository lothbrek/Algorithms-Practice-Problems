#order array by alphabet
#works with numbers and letters alike due to ruby's built in sort function

def alphabetize(arr,rev=false)
    if rev
        arr.reverse!
    else
        arr.sort!
    end
end

numbers = [5,1,2,4]
words = ["what", "is", "ruby?"]
puts("#{alphabetize(numbers)}")
puts("#{alphabetize(words)}")