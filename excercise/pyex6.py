from urllib.request import urlopen
# s = """
# <body bgcolor="#FFFFFF">
# Click<a href="http://www.python.org/"> Here </a>
# To connect to the most powerful tools in the world.
# </body>
# </html>
# """

def remove_tag(s):
    skip = False
    result = ''
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
            if type(c) == type(int):
                result += str(c)
            else:
                result += c

    return result

s = urlopen('http://www.python.org').read().decode('utf-8')
print('*'*40)
r = remove_tag(s)
print(r)

