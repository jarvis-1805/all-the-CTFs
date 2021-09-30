dic_keys = 'cringe cr1nge cRinge crIng3 cRimG3 cR1Ng3e criNgee CRINGE crinGE ccR1nge CriNGE cRINGe cr1ngE cringE CRIng3 Cr1nGe cR1nnge cR1Ng3 CrInGe cRingE cR1NGE CRiNg3 CRINGe CR1NGe cring3 CRIMNGE cRInGE crinG3 cRInge cRinG3 criNG3 cr1NG3 crinGe cRiNge CrInGE CRinGE'.split(' ')

dic_values = 'a b c d e f g h i j k l m n o p q r s t u v w x y z 0 1 2 3 4 5 6 7 8 9'.split(' ')

dic = dict(zip(dic_keys, dic_values))

encoded_flag = 'cR1Ng3e crinG3 cringE cringe cRINGe cRINGe cring3 crinG3 cringE cringE cRinG3 Cr1nGe cRimG3 criNG3 cRinge cRimG3 cringe cR1Ng3e cRiNge cRinG3 cR1Ng3 CrInGe cRInGE cr1ngE criNG3 cringE cring3 cRinge cR1Ng3 crinGE cringE criNgee cRinG3 CrInGe'.split(' ')

flag = ''

file = open('flag.txt', 'w')

for key in encoded_flag:
  flag += dic[key]

file.write('TamilCTF{' + flag + '}')
file.close()
print('Completed...')