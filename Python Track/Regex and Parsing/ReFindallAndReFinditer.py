import re

vowels = "aeiou"
cons = "qwrtypsdfghjklzxcvbnm"

m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (cons, vowels, cons), raw_input(), flags = re.I)

print('\n'.join(m or ['-1']))
