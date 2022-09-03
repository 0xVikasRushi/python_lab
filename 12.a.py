
import re
# /S	Matches any non-whitespace character
s = '''vikas@gmail.com to rushi@gmail.com'''
list = re.findall('\S+@+\S+',s)
print(list)



