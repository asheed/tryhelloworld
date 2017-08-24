s = """
<body bgcolor="#FFFFFF">
Click<a href="http://www.python.org/"> Here </a>
To connect to the most powerful tools in the world.
</body>
</html>
"""
skip = False
for c in s:
    if c == '<':
        skip = True
        continue
    elif c == '>':
        skip = False
        continue

    if skip:
        continue
    else:
        print(c, end='')

