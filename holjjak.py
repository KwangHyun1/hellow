# AI 컴퓨터가 홀짝문제를 내는데 우리가 맞춰야된다
import random
holjjak = '홀', '짝'
n = int(input('몇번 게임을 할 것 인지 입력하시오: '))


for i in range(n):
    user = input("홀짝을 선택하시오: ")
    com = random.choice(holjjak)
    if user == com:
        print(f"{i+1}/{n} 게임")
        print(f"{com} 입니다 통과")
    else:
        print(f'{i+1}/{n}')
        print('실패')
        quit()
print("럭키가이")