import random

for i in range(5):
    print(f'{i+1}. hellow world')
    print("짜장면이냐 짬뽕이냐?")

    a = input('먹고 싶은거 입력:')

    print(f'너가 입력한 값: {a}')

    menu = '짜장', '짬뽕'
    if a == '짜장' or  a == '짬뽕' :
        print(a)

        print(random.choice(menu)," 먹어")
    else:
        print("짬짜면")


