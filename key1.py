dic = { 'name': 'pey', 'phone':'01199933323', 'birth': '1118' }

dic['name']
dic['phone']
dic['birth']

a = { 1: 'hi'}
b = { 'a': [1, 2, 3]}
movie = {'스파이더맨': [220000, '2017-08-01', 1000] }

hobby = {
         "김연아":
             {
                 "취미":
                  ["피겨스케이팅", "LOL", "StarCraft2"],
                 "좋아하는것":
                  ['아이스크림']
             },
         "류현진":
             ["야구", "피파온라인"],
         "박지성":
             "축구",
         "귀도":
             "파이썬"
         }

print(hobby.keys())
print(hobby.values())
print(hobby.items())

# print(hobby['김연아'])
# print(hobby['귀도'])

for k in hobby.keys():
    print(hobby[k])

print('김연아1' in hobby)
