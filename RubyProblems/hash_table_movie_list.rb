#Create a listing of movies and functions to add, update, display, and 
#delete the selected title.

#This code was written to practice Ruby's implementation of hash tables.

movies = {
    "Lotr" => 10
}

puts "Please choose to add, update, display, or delete your movie titles and ratings: "
choice = gets.chomp

case choice
when "add"
    puts "What is your favorite movie title?"
    title = gets.chomp
    puts "What is your rating for that title?"
    rating = gets.chomp
    if movies[title.to_sym] == nil
        movies[title.to_sym] = rating.to_i
    else
        puts "That movie is already in the database!"
    end
    puts "#{title} has a rating of #{rating} for you!"
when "update"
    puts "Please input a movie title: "
    title = gets.chomp
    if movies[title] == nil
        puts "The movie is not in the hash, please remedy this."
    else
        puts "Please update the movie rating: "
        rating = gets.chomp
        movies[title.to_sym] = rating.to_i
    end
when "display"
  movies.each do |movie, rating|
    puts "#{movie}: #{rating}"
  end
    
when "delete"
    puts "Please input the title to delete: "
    del = gets.chomp
    
    if del == nil
        puts "The selected title does not exist."
    else
        movies.delete(del)
    end
end