#!/usr/bin/env ruby
puts AGRV[0].scan(/(?<=from:|to:|flags:).+?(?=\]).join(',')
