
milk_order = {'101':
                  {'서울유유(200ml)':1, '남양 요구르트': 5, '매일 우유(200ml)': 10},
              '102':
                  {'서울우유(500ml)':2},
              '103':
                  {'남양우유(1L)': 1, '남양 요구르트': 10},
              '104':
                  {'서울 요구르트': 15}
              }

for k, v in milk_order.items():
    print("{} 호 : ".format(k))
    for k1, v1 in v.items():
        print("{} - {}개".format(k1, v1))