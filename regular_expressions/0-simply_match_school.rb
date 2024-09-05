#!/usr/bin/env ruby
# This Ruby script accepts one argument and uses a regular expression to match "School"

puts ARGV[0].scan(/School/).join
