s = '''first line
second line
third line'''

print(':'.join(s.splitlines()))

print(s.splitlines()[1].split()[0])

print(':'.join(' '.join(s.splitlines()).split()))