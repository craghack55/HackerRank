import re

s = str(raw_input())

print "\n".join([i for i in re.split("[.,]+", s) if i])