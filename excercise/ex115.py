# s = 'first line\nsecond line\nthird line'

s = '''first line
second line
third line'''

# first line:second line:third line
s = s.splitlines()
# s = ['first line', 'second line', 'third line']
print(s[1].split()[0])
# s[1] = 'second line'
# s[1].split()
#
