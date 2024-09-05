#!/usr/bin/env ruby
#
log = ARGV[0]
sender = log.scan(/\[from:(.*?)\]/).flatten.first
receiver = log.scan(/\[to:(.*?)\]/).flatten.first
flags = log.scan(/\[flags:(.*?)\]/).flatten.first

puts "#{sender},#{receiver},#{flags}"
