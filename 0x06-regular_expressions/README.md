Regular Expression
Each file in this repository holds code that illustrates an essential concept of programming, specific to regular expressions. Resources to learn topic: rubular, regex101.com, blog

Environment
Language: Ruby
OS: Ubuntu 14.04 LTS
Usage: Run each file with ./[filename] "pattern to test if match" | cat -e
Each file has the following format:

# !/usr/bin/env ruby
puts ARGV[0].scan(/ regex here /).join

Authors
Karivone
