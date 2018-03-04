# -*- coding: utf-8 -*-

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x for x in L1 if isinstance(x, str)]

print(L2)

if L2 == ['Hello', 'World', "Apple"]:
    print('Succeed')
else:
    print("Failed")
