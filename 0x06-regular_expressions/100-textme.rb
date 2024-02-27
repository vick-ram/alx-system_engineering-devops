#!/usr/bin/env ruby

# Read each line from the log file provided as command line argument
ARGF.each do |line|
  # Extract sender, receiver, and flags information using regex
  match_data = line.match(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
  
  # If match_data is not nil, extract sender, receiver, and flags
  if match_data
    sender = match_data[1]
    receiver = match_data[2]
    flags = match_data[3]
    
    # Print the extracted information in the required format
    puts "#{sender},#{receiver},#{flags}"
  end
end
