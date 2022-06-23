import random


print("hellow, world!!")
print("짜장면이냐 짬뽕이냐?")
'''주석1 문자열 인식 '''
# 주석2 만약에 짜장과 짬뽕 둘중에 하나 추천
# 내가 짜장이나 짬뽕을 적으면 짜장이나 짬뽕 추천 아니면 둘다(짬짜면)
a = input('먹고 싶은거 입력:')
#print('너가 입력한 값:', a)
#print('너가 입력한 값: %s' %a)
#print('너가 입력한 값: {0}' .format(a))
print(f'너가 입력한 값: {a}')

menu = '짜장', '짬뽕'
if a == '짜장' or  a == '짬뽕' :
    print(a)
    # 인공지능이 추천해주는 결과는 ?
    print(random.choice(menu)," 먹어")
else:
    print("짬짜면")
# 아니면 둘다(짬짜면)

