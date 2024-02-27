#!/usr/bin/env ruby
def match_school(input)
  pattern = /School/
  match = input.scan(pattern)
  puts match.join('') ? match[0] : ''
end

input = ARGV[0]
match_school(input)
