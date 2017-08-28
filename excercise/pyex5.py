s = '''first line
second line
third line'''

# 115
print(':'.join(s.splitlines()))

# 116
print(s.splitlines()[1].split()[0])


print(':'.join(' '.join(s.splitlines()).split()))