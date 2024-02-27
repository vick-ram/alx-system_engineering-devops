#!/usr/bin/env ruby
# The regular expression must match /h[ot]+/
# Get the argument from the command line
input = ARGV[0]
# Define the regular expression
regex = /h[ot]+/
# Use the match method to check if the input matches the regular expression
match = input.match(regex)
# Print the match or a message if there is no match
if match
  puts match[0]
else
  puts "No match"
end
