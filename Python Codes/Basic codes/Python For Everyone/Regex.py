import re

str = 'X-DSPAM-Confidence:0.8475'
str_regex = r'\d\.\d+'

match = re.search(str_regex, str)
print(match.group())